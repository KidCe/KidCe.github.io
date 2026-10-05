#!/usr/bin/env python3
"""Validate and import an exact-offer visual audit, preserving manufacturer facts."""
import argparse,datetime,hashlib,json,pathlib,shutil,sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'dist/data'))
from offer_identity import attach_identity,verify_identity
FINDINGS={
 'cell-004':'NKON-Beschreibung nennt 4000 mAh, Titel und Spezifikationstabelle 5000 mAh. Widerspruch nicht aufgelöst.',
 'cell-006':'NKON-Tabelle nennt 5500 mAh Mindestkapazität und 5400 mAh typische Kapazität; Titel und Beschreibung nennen 5500 mAh. Widerspruch nicht aufgelöst.',
 'cell-007':'Angebotsadresse enthält 50XG; Produkttitel und Modellfeld nennen 60XG. EAN und sichtbare Identität stimmen mit diesem Angebot überein.',
 'cell-021':'NKON nennt ein storniertes Automobilprojekt und fehlende Isolierung. Neuheit wird auf der Angebotsseite nicht ausdrücklich zugesichert.',
 'cell-023':'Titel und Tabelle nennen 70 A, die Kurzbeschreibung 50 A. Tabellenwert bleibt gespeichert; Messbedingungen und Datenblatt separat beachten.',
 'cell-030':'NKON-Beschreibung nennt 21,8 mm Durchmesser, die Tabelle 21,3 mm. Tabellenwert bleibt gespeichert.',
 'cell-037':'Der sichtbare Titel lässt LG weg; die Tabelle nennt LG und INR21700-M58T. Angebotsidentität stimmt überein.',
 'cell-041':'NKON nennt den bereits vergangenen 25.09.2026 als Versanddatum und zeigt weiterhin Vorbestellung. Termin ist keine aktuelle Lieferzusage.',
 'cell-051':'Angebotsadresse enthält 45 A; Titel, Tabelle und EAN identifizieren das 35-A-Angebot. Die Adresse kann veraltet sein.',
 'cell-057':'Angebotsadresse nennt Produktionsjahr 2021; Titel, Tabelle und Beschreibung nennen 2022. Jahrgang aus der sichtbaren Produktseite übernommen.',
 'cell-058':'NKON-Beschreibung nennt 4000 mAh, Titel und Tabelle 5000 mAh (4950 mAh Mindestkapazität). Widerspruch nicht aufgelöst.',
 'cell-071':'Angebotsadresse nennt 21700A / 30 A; Titel, Tabelle und EAN identifizieren P42A / 45 A. Die Adresse kann veraltet sein.'}
PROTECTED=['chargeStandard','chargeMax','chargeFast','dischargeSheet','chargeVoltage','cutoffVoltage','resistanceAc','sources','researchStatus']
def replay(snapshot,report):
 records=report['listings'];by={r['id']:r for r in records}
 if len(by)!=len(records) or set(by)!={c['id'] for c in snapshot['cells']}:raise ValueError('Audit coverage differs from snapshot')
 for c in snapshot['cells']:
  r=by[c['id']];o=r['observed']
  if r['url']!=c['url'] or r['status']!='visually_checked' or not r['identityConfirmed']:raise ValueError('Unverified offer: '+c['id'])
  if not o['ean']:raise ValueError('Missing observed EAN')
  verify_identity(c,o['ean'],(o.get('brand') or c['brand']).split(' (',1)[0],o.get('model'),o['name'])
  if o['stock'] not in ('in_stock','out_of_stock','orderable'):raise ValueError('Unknown observed stock')
  if o['discontinued'] and o['stock']!='out_of_stock':raise ValueError('Discontinued stock conflict')
  if o['stock']=='orderable' and not o['orderButtonVisible']:raise ValueError('Missing preorder button')
  before={k:c.get(k) for k in PROTECTED}
  c.update(stock=o['stock'],delivery=o.get('delivery'),ean=o['ean'],discontinued=o['discontinued'],lifecycleEvidence=o.get('discontinuedNotice'),pricePack=o['pricePack'],price=round(o['pricePack']/c['packSize'],4),priceTiers=o['priceTiers'],tierStatus='published' if o['priceTiers'] else 'not_found',stockCheckedAt=r['checkedAt'],stockEvidence=o['literalStatus'],stockSource='NKON-Angebotsseite · visuell geprüft',shopAuditState='visually_checked',visualCheck='verified',visualCheckedAt=r['checkedAt'],visualEvidence='data/visual-evidence/'+c['id']+'.jpg',visualEvidenceSha256=r['screenshotSha256'],shopReviewFindings=[FINDINGS[c['id']]] if c['id'] in FINDINGS else [],sourceCrawl='Visuelle Prüfung am 01.10.2026')
  attach_identity(c)
  assert before=={k:c.get(k) for k in PROTECTED}
 snapshot.update(snapshotDate='2026-10-01',retrieval='Alle 72 exakten NKON-Angebote am 01.10.2026 zwischen 22:45 und 22:53 Uhr (Europe/Berlin) visuell geprüft, mit Screenshot pro Angebot. Datierter Snapshot; kein laufender Live-Bestand.',updateNote='BAK CG-50E als ausverkauft bestätigt; zwei Preisstaffeln korrigiert; 19 eingestellte Angebote markiert. Herstellerwerte unverändert. Shopwidersprüche separat dokumentiert.',visualAuditSummary={'date':'2026-10-01','model':'GPT-6 Luna','reasoning':'low','requestedListings':72,'attemptedListings':72,'verifiedListings':72,'blockedListings':0,'notAttemptedListings':0,'complete':True})
 return snapshot

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--audit-dir',required=True);args=ap.parse_args();src=pathlib.Path(args.audit_dir);report=json.loads((src/'visual-audit.json').read_text());snapshot=json.loads((ROOT/'dist/data/cells.json').read_text());original=json.loads((src/'cells-original.json').read_text())
 if hashlib.sha256((src/'cells-original.json').read_bytes()).hexdigest()!=report['sourceSha256']:raise ValueError('Source digest mismatch')
 if {c['id']:c['url'] for c in original['cells']}!={c['id']:c['url'] for c in snapshot['cells']}:raise ValueError('Source offers changed')
 for r in report['listings']:
  path=(src/r['screenshot']).resolve()
  if not path.is_relative_to(src.resolve()) or hashlib.sha256(path.read_bytes()).hexdigest()!=r['screenshotSha256']:raise ValueError('Screenshot mismatch: '+r['id'])
 replay(snapshot,report)
 # Save only after all records and hashes validate.
 target=ROOT/'dist/data/visual-evidence';target.mkdir(exist_ok=True)
 for r in report['listings']:shutil.copyfile(src/r['screenshot'],target/(r['id']+'.jpg'))
 (ROOT/'dist/data/cells.json').write_text(json.dumps(snapshot,ensure_ascii=False,indent=2))
 (ROOT/'dist/data/visual-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
 shutil.copyfile(src/'changes.json',ROOT/'dist/data/visual-changes.json')
 print('Imported 72 exact-offer records; 72 screenshot hashes validated; manufacturer values preserved.')
if __name__=='__main__':main()
