import json,re,pathlib,hashlib,runpy,sys

ROOT=pathlib.Path(__file__).resolve().parents[1]; S=ROOT/'scripts'
sys.path.insert(0,str(ROOT/'dist/data'))
classify_condition=runpy.run_path(str(ROOT/'dist/data/update_nkon.py'))['classify_condition']
def txt(f):return '\n'.join(c.get('text','') for c in json.loads(f.read_text())['content'])
def number(v):
 m=re.search(r'[-+]?\d+(?:[.,]\d+)?',v or '')
 return float(m[0].replace(',','.')) if m else None
def header(t):
 m=re.search(r'^(.+) \((https://[^)]+)\)\n【(turn\w+)】',t)
 return m
seed=json.loads((S/'catalog-seed.json').read_text()); records={}
for f in sorted(S.glob('details-*.json'))+sorted(S.glob('product-*.json')):
 for t in txt(f).split('\n--------------------------------------------------------------------------------\n'):
  h=header(t)
  if not h:continue
  if f.name.startswith('product-'):key=f.stem.replace('product-','')
  else:
   m=re.search(r'Source: click\(\{"ref_id":"(turn\w+)","id":(\d+)\}',t)
   key=next((c['id'] for c in seed if m and c['categoryRef']==m[1] and c['linkId']==int(m[2])),None)
  if key:records[key]=(t,h)
docs={}
for f in S.glob('datasheet*.json'):
 t=txt(f)
 for part in t.split('\n--------------------------------------------------------------------------------\n'):
  m=re.search(r'\((https://[^)]+)\)\n【(turn\w+)】',part)
  if m:docs[f.stem]={'url':m[1],'ref':m[2]}
def ds(i):return docs.get('datasheet-'+str(i),{}).get('url')
# Reviewed manufacturer specifications; current units A, resistance mOhm. Null is explicitly unknown.
# fast-charge profiles are kept separate from a stated maximum.
registry={
'BAK|50D2':(6,2.475,15,60,'80 °C Entladeabschaltung; Shopbeschreibung nennt zusätzlich 15 A.',None),
'BAK|45D':(29,2.2,13.2,60,'30 A ohne / 60 A mit 80 °C Abschaltung.',None),
'BAK|CD-53E':(15,2.575,5.15,10.3,'Maximalwerte bei 25 °C; nicht für zugesicherte Zyklenlebensdauer.',None),
'BAK|CH-58E':(43,2.8,5.6,11.2,'Maximalwerte bei 25 °C; nicht für zugesicherte Zyklenlebensdauer.',None),
'BAK|N21700CG-50E':(21,2.5,5,15,'C-Raten aus 5 Ah umgerechnet. Datenblatt 15 A; Shop 14,7 A.',13),
'BAK|N21700CG':(23,2.5,5,15,'C-Raten aus 5 Ah umgerechnet. Datenblatt 15 A; Shop 10,2 A. Revision prüfen.',None),
'Tenpower|60XG':(0,3,16,60,'Entladung nur mit 75 °C Abschaltung; Datenblatt V0.1 draft.',5),
'Tenpower|30SG':(7,1.5,6,30,'Hersteller-Produktdatenblatt v1.4.',15),
'Tenpower|40XG':(34,2,12,45,'Entladebedingungen und Temperaturgrenzen im Datenblatt beachten.',None),
'Tenpower|50XG':(40,2.5,15,40,'Entladebedingungen und Temperaturgrenzen im Datenblatt beachten.',None),
'Tenpower|40TG':(26,2,6,35,'Hersteller-Produktdatenblatt v1.4.1.',10),
'Tenpower|50SG':(42,2.5,6,20,'Standard 2500 mA; maximal 6 A.',None),
'EVE|50E':(19,1,2.5,15,'Herstellerdatenblatt: Standard 1000 mA; maximal 2500 mA.',None),
'EVE|58E':(13,1.12,5.6,16.8,'Datenblatt bezieht sich auf 5600 mAh; Shop nennt 5700 mAh. Maximalwerte nicht für Zyklenlebensdauer.',None),
'EVE|40PL':(16,2,8,70,'75 °C Abschaltung empfohlen; 80 °C absoluter Grenzwert.',None),
'EVE|40P':(20,2,None,50,'6 A ist als Schnellladeprofil angegeben, nicht ausdrücklich als Maximum; 80 °C Entladeabschaltung.',None),
'EVE|50PL':(31,2.5,10,125,'75 °C Abschaltung empfohlen; 80 °C maximal. Revision A, neue Version.',None),
'DMEGC|50E':(12,2.5,5,15,'0,5 C / 1 C aus 5 Ah umgerechnet.',None),
'Molicel|M65A':(2,6.5,6.5,26,'Vorläufige Spezifikation 0.1; 80 °C Entladeabschaltung empfohlen; Zelloberfläche beim Laden ≤70 °C.',14.5),
'Molicel|P50B':(24,5,25,60,'70 °C Ladeabschaltung / 80 °C Entladeabschaltung; Datenblatt Version 1.1.',6.5),
'Molicel|P45B':(41,4.5,13.5,45,'70 °C Ladeabschaltung / 80 °C Entladeabschaltung; Version 1.2.',7),
'Molicel|P42A':(38,4.2,None,45,'Einseitiges Datenblatt nennt nur Standardladestrom. Zusätzliche Spezifikation ergänzt Maximum.',10),
'Molicel|M50A':(39,2.5,None,15,'Maximaler Ladestrom im gefundenen Produktdatenblatt nicht ausdrücklich spezifiziert.',15),
'Samsung|50G':(1,1.6,4.85,9.7,'Tentative Version 0.1; 1 C = 4850 mA.',None),
'Samsung|50GB':(28,2.45,4.9,9.7,'Maximaler Ladestrom nicht für zugesicherte Zyklenlebensdauer.',None),
'Samsung|53G2':(32,1.749,5.3,15.9,'Maximalwerte nicht für zugesicherte Zyklenlebensdauer.',None),
'Samsung|50E':(37,2.45,4.9,9.8,'Maximaler Ladestrom nicht für zugesicherte Zyklenlebensdauer.',None),
'Samsung|45T':(36,2.25,6,50,'35 A ohne / 50 A mit 80 °C Abschaltung. 9 A nur für Step-Charge, nicht kontinuierlich.',None),
'XTAR|6000':(11,3,4.2,10,'Geschützte Zelle; Innenwiderstand ≤45 mΩ.',45),
'Keeppower|P2160TC':(27,1.2,4.2,10,'Externer Li-Ion-Lader; USB-C-Ladung separat. Standardstrom im PDF als 1200mAh geschrieben (Einheitenfehler).',45),
'Keeppower|P2150TC':(17,.97,4.85,8,'Externer Li-Ion-Lader. USB-Eingang und interner Ladestrom sind separate Angaben.',None),
'Reliance|RS60':(5,3,12,50,'80 °C Entladeabschaltung; max. Ladestrom 12 A ab 15 °C, unter 15 °C nur 3 A.',None),
'Reliance|RH60':(9,3,6,20,'80 °C Entladeabschaltung.',None),
'Reliance|RS50':('extra-2',2.5,15,70,'80 °C Entladeabschaltung; temperaturabhängige Ladegrenzen siehe Spezifikation.',None),
'Ampace|JP50':('extra-0',2.5,15,60,'40 A ohne / 60 A mit 80 °C Abschaltung. Maximaler Ladestrom laut Herstellerseite 15 A.',4),
'Ampace|JP40':('extra-1',2,8,45,'Verlinkte Spezifikation nennt 45 A; aktuelle Herstellerseite 40 A Full-Discharge / 60 A Maximum. Shop 70 A. Revisionen unterscheiden sich.',None),
}
# Persist the human-reviewed registry independently of changing shop data.
(S/'spec-registry.json').write_text(json.dumps(registry,ensure_ascii=False,indent=2))
out=[]
for c in seed:
 t,h=records.get(c['id'],('',None));spec={k.strip():v.strip() for k,v in re.findall(r'L\d+: ([^\n|]+)\s+\|\s*([^\n]+)',t)}
 name=c['name']; brand=spec.get('Marke',name.split(' ')[0]);model=spec.get('Modell')
 if brand=='2x':brand='Keeppower'
 if brand=='**':brand='Nicht genannt'
 match=None
 for key,v in registry.items():
  b,m=key.split('|')
  if brand==b and (m in (model or '') or (m in name)):
   if match is None or len(m)>len(match[0].split('|')[1]):match=(key,v)
 # 50G and 50GB / CG and CG-50E use longest specific match.
 pack=2 if name.startswith('2x ') else 1
 weight=number(spec.get('Gewicht - g'));weight=weight/pack if weight else None
 current=number(spec.get('Entladestrom - A')) or c['dischargeShop'];cap=number(spec.get('Typ. Kapazität - mAh')) or c['capacity'];voltage=number(spec.get('Spannung'))
 stock=c['stock']; delivery=None
 if re.search(r'L\d+: Nicht auf Lager',t):stock='out_of_stock'
 elif re.search(r'L\d+: Auf [Ll]ager',t):stock='in_stock'
 elif (dt:=re.search(r'L\d+: (\d{1,2}-\d{1,2}-\d{4})\s*\n',t)) and 'In den Einkaufswagen' in t:
  stock='orderable';delivery=dt[1]
 elif 'In den Einkaufswagen' in t:stock='unknown'
 # Only explicit out-of-stock evidence maps to that state. Dates + ordering indicate backorder, even past dates.
 if not t and stock=='unknown':stock='unknown'
 priceMatch=re.search(r'L\d+: (?:Special Price )?(\d+,\d+)\s*€',t);price=float(priceMatch[1].replace(',','.')) if priceMatch else c['pricePack']
 ver=spec.get('Batterieversion','');condition='reclaimed' if re.search('Reclaimed|Renoviert|zurückgefordert',name+' '+ver,re.I) else 'mixed' if re.search('mixed|Mischcharge',name+' '+ver,re.I) else 'new'
 cell={**c,'brand':brand,'model':model or re.sub(r'\s+\d+\s*mAh.*','',name,flags=re.I),'capacity':cap,'minCapacity':number(spec.get('Mindest. kapazität - mAh')),'dischargeShop':current,'pricePack':price,'packSize':pack,'price':round(price/pack,4),'weight':weight,'voltage':voltage,'height':number(spec.get('Höhe - mm')),'diameter':number(spec.get('Durchmesser - mm')),'protected':spec.get('Sicherung','').lower() not in ('ohne','') or bool(re.search(r'\bprotected\b|\bgeschützt\b',name,re.I)),'condition':condition,'terminal':ver,'stock':stock,'delivery':delivery,'url':h[2] if h else None,'chargeStandard':None,'chargeMax':None,'chargeFast':None,'dischargeSheet':None,'chargeVoltage':None,'cutoffVoltage':None,'resistanceAc':None,'notes':[],'sources':[],'researchStatus':'Kein passendes Herstellerdatenblatt gefunden','retrievedAt':'2026-10-01','sourceCrawl': re.search(r'Crawled: ([^;]+);',t)[1] if re.search(r'Crawled: ([^;]+);',t) else 'today'}
 cell['priceTiers']=[{'minPacks':int(q),'pricePack':float(p.replace('.','').replace(',','.'))} for q,p in re.findall(r'Kaufen\s+(\d+)\s+Stück\s+für\s+([\d.,]+)',t)]
 cell['tierStatus']='published' if cell['priceTiers'] else 'not_found'
 cell['conditionCategory'],cell['conditionEvidence']=classify_condition(t.split('Write Your Own Review')[0],condition)
 if match:
  k,v=match;i,standard,maximum,discharge,note,ir=v
  cell.update(chargeStandard=standard,chargeMax=maximum,dischargeSheet=discharge,chargeVoltage=4.2,cutoffVoltage=2.5,resistanceAc=ir,researchStatus='Herstellerdatenblatt geprüft')
  cell['notes'].append(note);cell['sources'].append({'label':'Herstellerdatenblatt','url':ds(i),'section':'Lade- und Entladespezifikationen'})
  if k=='EVE|40P':cell['chargeFast']=6
  if k=='Molicel|P42A':
   cell['chargeMax']=8.4;cell['sources'].append({'label':'Ausführliche P42A-Spezifikation','url':'https://www.nkon.nl/de/amfile/file/download/file/1588/product/5985/','section':'Rated specifications: maximum charging current'})
  if k=='Ampace|JP50':cell['sources'].append({'label':'Aktuelle Herstellerparameter','url':'https://en.ampace.com/products/power-tools-product-matrix/jp/69'})
  if k=='Ampace|JP40':cell['sources'].append({'label':'Aktuelle Herstellerparameter','url':'https://en.ampace.com/products/power-tools-product-matrix/jp/68'})
 # Exact manufacturer variant matters; do not carry charge currents to unmatched variants.
 if brand=='Samsung' and '58E' in name:
  ii=22 if 'Reclaimed' in name else 33 if 'mixed' in name else None
  if ii is not None:
   cell.update(chargeStandard=2.665 if ii==22 else 1.066,chargeMax=5.33,dischargeSheet=10.66,chargeVoltage=4.2,cutoffVoltage=2.5,researchStatus='Herstellerdatenblatt geprüft');cell['sources'].append({'label':'Herstellerdatenblatt','url':ds(ii)});cell['notes'].append('C-Raten aus 5330 mAh umgerechnet; Maximalwerte nicht für Zyklenlebensdauer. Batch-/Revisionszuordnung beachten.')
 if brand=='Samsung' and '50S' in name:
  cell.update(chargeStandard=2.5,chargeMax=6,dischargeSheet=45,chargeVoltage=4.2,cutoffVoltage=2.5,resistanceAc=14,researchStatus='Herstellerdatenblatt geprüft');cell['sources'].append({'label':'Samsung Spezifikation V1.0','url':'https://www.nkon.nl/en/amfile/file/download/file/167/product/4821/'});cell['notes'].append('25 A ohne / 45 A mit 80 °C Abschaltung. Shop 35 A. V1.0 (2021).')
 if brand=='Samsung' and '30T' in name:
  cell.update(chargeStandard=1.5,chargeFast=4,dischargeSheet=35,chargeVoltage=4.2,cutoffVoltage=2.5,resistanceAc=15,researchStatus='Herstellerdatenblatt geprüft');cell['sources'].append({'label':'Samsung 30T Spezifikation V2.0','url':'https://www.nkon.nl/en/amfile/file/download/file/206/product/2902/'});cell['notes'].append('4 A als Rated-/Rapid-Charge angegeben, nicht ausdrücklich als Maximum. Ladetemperatur 0–50 °C; Entladung −20–80 °C.')
 if cell['chargeMax'] is None:cell['notes'].append('Maximaler Ladestrom nicht belegt; kein Wert aus Entladestrom abgeleitet.')
 if condition!='new':cell['notes'].append('Zustand/Charge des Angebots separat vom Datenblatt einer neuen Zelle bewerten.')
 if delivery:cell['notes'].append('NKON zeigt Bestellmöglichkeit mit Datum '+delivery+'. Lieferstatus ist ein Snapshot; Datum kann veraltet sein.')
 if brand=='Lishen' and cap and c['capacity']!=cap:cell['notes'].append('Produkttitel und Tabelle widersprechen sich: Titel '+str(c['capacity'])+' mAh, Tabelle '+str(cap)+' mAh.')
 if cell['sources']:cell['sources']=[s for s in cell['sources'] if s.get('url')]
 cell['sources'].insert(0,{'label':'NKON Angebot','url':cell['url']})
 for field in ['linkId','categoryRef','categoryPage']:cell.pop(field,None)
 out.append(cell)
snapshot={'schemaVersion':1,'snapshotDate':'2026-10-01','retrieval':'Rechercheindex; kein verifizierter Live-Bestand. Quellen können unterschiedliche Abrufstände haben.','categoryUrl':'https://www.nkon.nl/de/rechargeable/li-ion/21700-20700-size.html','expectedCount':72,'completeCatalog':len(out)==72,'cells':out,'updateNote':'Direkter HTTP-Abruf war durch Cloudflare gesperrt. Wiederholbarer Importer liegt bei; der Live-Pfad konnte deshalb noch nicht vollständig validiert werden.'}
(ROOT/'dist/data/cells.json').write_text(json.dumps(snapshot,ensure_ascii=False,indent=2)); print('Cells:',len(out),'standard:',sum(x['chargeStandard'] is not None for x in out),'max:',sum(x['chargeMax'] is not None for x in out));print('stock', {s:sum(x['stock']==s for x in out) for s in ['in_stock','orderable','out_of_stock','unknown']})

# Apply the exact-offer review after rebuilding the original seed.
from audit_snapshot import apply
review=apply(snapshot,replay_index_first=True)
(ROOT/"dist/data/cells.json").write_text(json.dumps(snapshot,ensure_ascii=False,indent=2))
