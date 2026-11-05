#!/usr/bin/env python3
"""Refresh NKON 21700 shop facts, preserving reviewed cell specifications.
Requires requests and beautifulsoup4. Never uses an LLM; never bypasses bot checks.
Atomic commit only after complete pagination and all product pages were parsed.
"""
import argparse, datetime, hashlib, json, pathlib, re, sys, time
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
from offer_identity import attach_identity,offer_key,verify_identity
CATEGORY='https://www.nkon.nl/de/rechargeable/li-ion/21700-20700-size.html'

def numeric(s):
    m=re.search(r'\d+(?:[.,]\d+)?',str(s or '').replace('\xa0',''))
    return float(m[0].replace(',','.')) if m else None

def soup(html):
    if re.search(r'cf-mitigated|Just a moment|Performing security verification|verify you are human|challenges.cloudflare.com',html,re.I):
        raise RuntimeError('NKON security verification blocked this client. No changes were saved.')
    return BeautifulSoup(html,'html.parser')

def category(html,url):
    doc=soup(html);links=[]
    for a in doc.select('a.product-item-link, .product-item-name a'):
        href=urljoin(url,a.get('href',''))
        if urlparse(href).netloc not in ('www.nkon.nl','nkon.nl'):raise ValueError('Unexpected product host')
        if href not in links:links.append(href)
    text=doc.get_text(' ',strip=True)
    m=re.search(r'\d+\s*[-–]\s*\d+\s+(?:of|von)\s+(\d+)',text,re.I)
    pages=[urljoin(url,a['href']) for a in doc.select('.pages a[href]')]
    pages=list(dict.fromkeys(u for u in pages if urlparse(u).netloc in ('www.nkon.nl','nkon.nl')))
    if not links:raise ValueError('Category layout changed: no product links. Old snapshot retained.')
    return links,pages,int(m[1]) if m else None

def product(html,url,previous):
    doc=soup(html);heading=doc.select_one('h1.page-title, h1')
    if not heading:raise ValueError('Product title missing: '+url)
    name=heading.get_text(' ',strip=True); attrs={}
    for tr in doc.select('table tr'):
        fields=tr.find_all(['th','td'],recursive=False)
        if len(fields)>=2:attrs[fields[0].get_text(' ',strip=True).lower()]=fields[1].get_text(' ',strip=True)
    def a(*keys):return next((attrs[k] for k in keys if k in attrs),None)
    ean=a('ean / gtin','ean','gtin'); brand=a('merk','marke','brand') or name.split()[0]; model=a('model','modell') or name
    verify_identity(previous,ean,brand,model,name)
    old=dict(previous or {}); old['ean']=ean; pack=2 if re.match(r'2x\s',name,re.I) else 1
    old.update(id=old.get('id','nkon-'+hashlib.sha256(url.encode()).hexdigest()[:14]),name=name,url=url,packSize=pack)
    numeric_fields={'capacity':('typ. capaciteit - mah','typ. kapazität - mah','typ. capacity - mah'),'minCapacity':('min. capaciteit - mah','mindest. kapazität - mah','min. capacity - mah'),'dischargeShop':('ontlaadstroom - a','entladestrom - a','discharge current - a'),'voltage':('spanning','spannung','voltage'),'weight':('gewicht - g','weight - g'),'height':('hoogte - mm','höhe - mm','height - mm'),'diameter':('diameter - mm','durchmesser - mm')}
    # Never keep stale price/stock or shop measurements when the new page omits them.
    for key,keys in numeric_fields.items():old[key]=numeric(a(*keys))
    old['weight']=old['weight']/pack if old['weight'] is not None else None
    old['brand']=a('merk','marke','brand') or name.split()[0];old['model']=a('model','modell') or name
    p=doc.select_one('.price-box .special-price [data-price-amount], .price-box [data-price-type=finalPrice]') or doc.select_one('.price-box [data-price-amount]')
    if not p:raise ValueError('Price layout changed: '+url)
    price=numeric(p.get('data-price-amount'))
    if price is None:raise ValueError('Invalid product price: '+url)
    old['pricePack']=price;old['price']=round(price/pack,4)
    tiers=[]
    for li in doc.select('.prices-tier li, .tier-prices li'):
        text=li.get_text(' ',strip=True)
        match=re.search(r'(?:Kaufen|Buy|Koop)\s+(\d+)\s+(?:(?:Stück|pieces|stuks)\s+)?(?:für|for|voor)\s*€?\s*([\d.,]+)',text,re.I)
        if match:tiers.append({'minPacks':int(match[1]),'pricePack':numeric(match[2])})
    old['priceTiers']=sorted(tiers,key=lambda x:x['minPacks']);old['tierStatus']='published' if tiers else 'not_found'
    status=doc.select_one('.stock'); statusText=status.get_text(' ',strip=True).lower() if status else ''
    old['delivery']=None
    if re.search(r'niet|nicht|out of stock',statusText):old['stock']='out_of_stock'
    elif re.search(r'op voorraad|auf lager|in stock',statusText):old['stock']='in_stock'
    else:
        # Only treat a date as a backorder signal inside the stock area, never a review or footer date.
        date=re.search(r'\b(\d{1,2}-\d{1,2}-\d{4})\b',statusText)
        buy=doc.select_one('button#product-addtocart-button:not([disabled]), button.tocart:not([disabled])')
        old['stock']='orderable' if date and buy else 'unknown'
        old['delivery']=date[1] if date else None
    info=doc.select_one('.product-info-main') or doc
    lifecycle=re.search(r'dieses produkt wurde eingestellt(?: und wird nicht mehr aufgefüllt)?|this product (?:has been|is) discontinued|dit product is (?:stopgezet|uit productie)|niet meer aangevuld',info.get_text(' ',strip=True),re.I)
    # An explicit end-of-sale notice overrides date/buttons or conflicting stock markup.
    old['discontinued']=bool(lifecycle) or bool(old.get('discontinued') and not (old['stock']=='in_stock' and doc.select_one('button#product-addtocart-button:not([disabled]), button.tocart:not([disabled])')))
    old['lifecycleEvidence']=lifecycle[0] if lifecycle else old.get('lifecycleEvidence') if old['discontinued'] else None
    if old['discontinued']:old['stock']='out_of_stock';old['delivery']=None
    state=a('batterij versie','batterieversion','battery version') or ''
    old['terminal']=state;old['condition']='reclaimed' if re.search('reclaimed|renoviert|zurückgefordert',name+' '+state,re.I) else 'mixed' if re.search('mixed|mischcharge',name+' '+state,re.I) else 'new'
    description=doc.select_one('.product.attribute.description .value, #description .value')
    old['conditionCategory'],old['conditionEvidence']=classify_condition(description.get_text(' ',strip=True) if description else '',old['condition'])
    protection=a('bescherming','sicherung','protection')
    old['protected']=(protection or '').lower() not in ('','ohne','unprotected','no','zonder') or bool(re.search(r'\bprotected\b|\bgeschützt\b',name,re.I))
    if not previous:
        old.update(chargeStandard=None,chargeMax=None,chargeFast=None,dischargeSheet=None,chargeVoltage=None,cutoffVoltage=None,resistanceAc=None,researchStatus='Neues Angebot: Datenblattprüfung offen',notes=['Neues Modell oder neue Variante. Datenblattgrenzen wurden noch nicht geprüft.'],sources=[{'label':'NKON Angebot','url':url}])
    docs=[]
    for anchor in doc.select('a[href]'):
        if re.search(r'datasheet|specification|datenblatt',anchor.get_text(' ',strip=True),re.I):
            href=urljoin(url,anchor['href'])
            if href.startswith('https://'):docs.append({'label':anchor.get_text(' ',strip=True),'url':href})
    old.update(stockCheckedAt=datetime.date.today().isoformat(),stockEvidence=statusText+(' · '+(old.get('lifecycleEvidence') or 'Eingestellt') if old.get('discontinued') else ''),stockSource='Direct HTTP',shopAuditState='checked',visualCheck='not_attempted',visualCheckedAt=None,visualEvidence=None,visualEvidenceSha256=None)
    attach_identity(old)
    old['discoveredDocuments']=docs;old['retrievedAt']=datetime.date.today().isoformat();old['sourceCrawl']='direct HTTP'
    return old

def classify_condition(text,condition):
    if condition=='mixed':return 'mixed','NKON kennzeichnet das Angebot als Mischcharge; individuelle Vorgeschichte nicht belegt.'
    if condition!='reclaimed':return 'regular','Reguläres Angebot; keine Reclaimed- oder Mixed-Batch-Kennzeichnung in der Quelle.'
    never=re.search(r'(?:nie|niemals).{0,30}geladen.{0,25}entladen|never (?:been )?(?:charged|discharged)|never used',text,re.I|re.S)
    welding=re.search(r'schweißfehler|schweissfehler|weld(?:ing)? (?:fault|defect|error|issue)',text,re.I)
    if never and welding:return 'unused_pack_reject','NKON nennt Packausschuss mit Schweißfehlern und gibt an, dass die Zellen nie geladen oder entladen wurden.'
    if never:return 'unused_reclaimed','NKON beschreibt die Reclaimed-Zellen als unbenutzt; ein Schweißfehler ist nicht eindeutig belegt.'
    if re.search(r'(?:bereits|schon).{0,18}(?:gebraucht|benutzt|verwendet)|previously used|capacity (?:loss|reduction)|kapazitätsverlust',text,re.I):return 'used_reclaimed','NKON beschreibt vorherige Nutzung oder Kapazitätsverlust; individuelle Restkapazität nicht zugesichert.'
    return 'reclaimed_unknown','Reclaimed-Angebot ohne eindeutige Angabe zur vorherigen Nutzung. Keine Annahme einer neuwertigen Zelle.'

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--snapshot',default='cells.json');ap.add_argument('--output');ap.add_argument('--html-dir',help='Directory of saved category/product HTML with manifest.json mapping URLs to filenames');args=ap.parse_args()
    src=pathlib.Path(args.snapshot);snap=json.loads(src.read_text());old={offer_key(c['url']):c for c in snap['cells'] if c.get('url')};session=requests.Session();session.headers['User-Agent']='NKON-Cell-Selector/1.0 snapshot refresh';cache={};base=None
    if args.html_dir:
        base=pathlib.Path(args.html_dir);cache=json.loads((base/'manifest.json').read_text())
    def read(url):
        if base:
            if url not in cache:raise ValueError('Saved page missing: '+url)
            return (base/cache[url]).read_text()
        time.sleep(.6);r=session.get(url,timeout=30)
        if r.status_code in (403,429):raise RuntimeError('NKON rejected the request. Stop; old snapshot retained.')
        r.raise_for_status()
        if url in old and offer_key(r.url)!=offer_key(url):raise ValueError('Product redirected to another offer. Old snapshot retained.')
        return r.text
    queue=[CATEGORY];visited=set();urls=[];expected=None
    while queue:
        url=queue.pop(0)
        if url in visited:continue
        if len(visited)>=50:raise ValueError('Pagination exceeded limit')
        visited.add(url);links,pages,count=category(read(url),url);expected=expected or count
        urls.extend(u for u in links if u not in urls);queue.extend(u for u in pages if u not in visited)
    if expected is None or len(urls)!=expected:raise ValueError(f'Incomplete catalog ({len(urls)} / {expected}). Old snapshot retained.')
    fresh=[product(read(u),u,old.get(offer_key(u))) for u in urls]
    snap.update(cells=fresh,visualAuditSummary=None,snapshotDate=datetime.date.today().isoformat(),expectedCount=expected,completeCatalog=True,retrieval='Direct NKON HTTP or supplied HTML; all catalog pages and product pages parsed.',updateNote='Shopdaten erneuert. Vorhandene Datenblattprüfung übernommen; neue Angebote separat prüfen.')
    target=pathlib.Path(args.output or src);temp=target.with_suffix(target.suffix+'.tmp');temp.write_text(json.dumps(snap,ensure_ascii=False,indent=2));temp.replace(target)
    print(f'Updated {len(fresh)} offers. Snapshot saved to {target}')
if __name__=='__main__':
    try:main()
    except Exception as exc:print(str(exc),file=sys.stderr);sys.exit(1)
