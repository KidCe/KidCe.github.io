#!/usr/bin/env python3
"""Replay the dated, exact-offer NKON research audit without an LLM.
Does not replace the direct HTTP updater. Failed sources become unknown.
"""
import json,re,pathlib,collections,sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/"dist/data"))
from offer_identity import attach_identity,verify_identity
ROOT=pathlib.Path(__file__).resolve().parents[1]
def number(s):return float(s.replace('\xa0','').replace(',','.'))
def apply(snapshot,replay_index_first=False):
 # A complete newer visual review supersedes the older index replay.
 latest=ROOT/'dist/data/visual-audit.json'
 if latest.exists():
  visual=json.loads(latest.read_text())
  if visual.get('summary',{}).get('complete') and not replay_index_first:
   from import_visual_audit import replay
   replay(snapshot,visual)
   return {'date':'2026-10-01','offers':len(snapshot['cells']),'verifiedIndexedPages':0,'unavailable':[],'changes':[],'sourceConflicts':[],'statusCounts':dict(collections.Counter(c['stock'] for c in snapshot['cells'])),'supersededBy':'Complete visual audit'}
 changes=[]; failures=[];conflicts=[]
 for c in snapshot['cells']:
  attach_identity(c)
  raw=json.loads((ROOT/'scripts'/('audit-'+c['id']+'.json')).read_text())
  text='\n'.join(x.get('text','') for x in raw['content'])
  lines=[re.sub(r'^L\d+(?:@P\d+)?:\s*','',s).strip() for s in text.splitlines()]
  if 'Internal Error' in text or c['url'] not in text or not any(x.startswith('# ') for x in lines):
   if c['stock']!='unknown':changes.append({'id':c['id'],'name':c['name'],'field':'stock','before':c['stock'],'after':'unknown'})
   c.update(stock='unknown',stockCheckedAt='2026-10-01',stockEvidence='Angebotsseite nicht abrufbar; Bestand nicht bestätigt.',stockSource='Rechercheindex',delivery=None,shopAuditState='unavailable')
   failures.append({'id':c['id'],'url':c['url']});continue
  start=next(i for i,x in enumerate(lines) if x.startswith('# '));lines=lines[start:]
  end=next((i for i,x in enumerate(lines) if x=='Write Your Own Review'),len(lines));lines=lines[:end]
  attrs={x.split('|',1)[0].strip().lower():x.split('|',1)[1].strip() for x in lines if '|' in x}
  ean=attrs.get('ean / gtin');assert ean, c['id']
  if c.get('ean') and c['ean']!=ean:raise ValueError('Offer EAN changed: '+c['id'])
  verify_identity(c,ean,attrs.get('marke') or c['brand'],attrs.get('modell'),lines[0][2:])
  c['ean']=ean
  statuses=[x for x in lines if x in ('Nicht auf Lager','Auf Lager') or re.fullmatch(r'\d\d-\d\d-\d{4}',x)]
  assert len(statuses)==1,(c['id'],statuses)
  evidence=statuses[0];stock='out_of_stock' if evidence=='Nicht auf Lager' else 'in_stock' if evidence=='Auf Lager' else 'orderable'
  if stock=='orderable':assert 'In den Einkaufswagen' in lines,c['id']
  prices=[re.match(r'^(?:Special Price )?([\d.,]+)\s*€\s*Exkl',x) for x in lines];prices=[m for m in prices if m]
  assert prices,c['id']; price=number(prices[-1][1]) # final price, after any struck-through original
  tiers=[]
  for x in lines:
   m=re.search(r'Kaufen (\d+) Stück für ([\d.,]+)\s*€',x)
   if m:tiers.append({'minPacks':int(m[1]),'pricePack':number(m[2])})
  updates={'stock':stock,'delivery':evidence if stock=='orderable' else None,'pricePack':price,'price':round(price/c['packSize'],4),'priceTiers':tiers,'tierStatus':'published' if tiers else 'not_found','terminal':attrs.get('batterieversion',c.get('terminal')),'protected':attrs.get('sicherung','Ohne').lower() not in ('ohne','unprotected','no','zonder','')}
  fields={'capacity':'typ. kapazität - mah','minCapacity':'mindest. kapazität - mah','dischargeShop':'entladestrom - a','weight':'gewicht - g','voltage':'spannung','height':'höhe - mm','diameter':'durchmesser - mm'}
  for key,a in fields.items():
   s=attrs.get(a);m=re.search(r'\d+(?:[.,]\d+)?',s or '')
   if m:updates[key]=number(m[0])/(c['packSize'] if key=='weight' else 1)
  for k,v in updates.items():
   if c.get(k)!=v:changes.append({'id':c['id'],'name':c['name'],'field':k,'before':c.get(k),'after':v})
  attach_identity(c)
  c.update(updates,stockCheckedAt='2026-10-01',stockEvidence=evidence,stockSource='Rechercheindex',shopAuditState='checked',retrievedAt='2026-10-01',sourceCrawl=re.search(r'Crawled: ([^;]+)',text)[1])
  body='\n'.join(lines);m=re.search(r'Kapazität:\s*(\d+)\s*mAh',body)
  if m and int(m[1]) not in (c.get('capacity'),c.get('minCapacity')):
   note=f"NKON-Quellenwiderspruch: Beschreibung {m[1]} mAh, Spezifikationstabelle {c['capacity']:g} mAh. Tabellenwert verwendet."
   if note not in c['notes']:c['notes'].append(note)
   conflicts.append({'id':c['id'],'note':note})
  if c.get('minCapacity') is not None and c.get('capacity') is not None and c['minCapacity']>c['capacity']:
   note=f"NKON-Tabelle widersprüchlich: Mindestkapazität {c['minCapacity']:g} mAh liegt über typischer Kapazität {c['capacity']:g} mAh. Beide Shopangaben sind unbestätigt; keine Datenblattwerte."
   if note not in c['notes']:c['notes'].append(note)
 # Reviewed exact-offer evidence outranks the dated index replay.
 overrides=ROOT/'scripts/reviewed-shop-overrides.json'
 if overrides.exists():
  for o in json.loads(overrides.read_text()):
   c=next(c for c in snapshot['cells'] if c['url']==o['url'])
   if c.get('ean')!=o['ean']:raise ValueError('Override EAN mismatch')
   c.update(o);c['delivery']=None
 snapshot.update(snapshotDate='2026-10-01',retrieval='Alle 72 exakten Angebote am 01.10.2026 im Rechercheindex abgeglichen; 71 Angebotsseiten ausgewertet, 1 nicht abrufbar. Kein verifizierter Live-Bestand.',updateNote='Bestand, Preise, Staffelpreise und Shopkennwerte pro URL/EAN abgeglichen. Varianten bleiben getrennt. Nicht abrufbare Bestände sind unbekannt.')
 report={'date':'2026-10-01','offers':len(snapshot['cells']),'verifiedIndexedPages':len(snapshot['cells'])-len(failures),'unavailable':failures,'changes':changes,'sourceConflicts':conflicts,'statusCounts':dict(collections.Counter(c['stock'] for c in snapshot['cells']))}
 if latest.exists() and visual.get('summary',{}).get('complete'):
  from import_visual_audit import replay
  replay(snapshot,visual)
  report.update(supersededBy='Complete visual audit',statusCounts=dict(collections.Counter(c['stock'] for c in snapshot['cells'])))
 return report
if __name__=='__main__':
 p=ROOT/'dist/data/cells.json';snapshot=json.loads(p.read_text());report=apply(snapshot)
 p.write_text(json.dumps(snapshot,ensure_ascii=False,indent=2));
 if report['changes'] or not (ROOT/'dist/data/audit.json').exists():(ROOT/'dist/data/audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
 print(json.dumps({'changesByField':dict(collections.Counter(c['field'] for c in report['changes'])),'statusCounts':report['statusCounts'],'unavailable':report['unavailable'],'conflicts':report['sourceConflicts']},ensure_ascii=False))
