import unittest,json,pathlib,sys,copy
ROOT=pathlib.Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'dist/data'))
from update_nkon import product
from offer_identity import offer_key
class Offers(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.cells=json.loads((ROOT/'dist/data/cells.json').read_text())['cells']
 def test_three_50me_listings(self):
  offers=[c for c in self.cells if c['brand']=='Tenpower' and c['model']=='INR21700-50ME']
  self.assertEqual(len(offers),3);self.assertEqual(len({c['offerKey'] for c in offers}),3);self.assertEqual(len({c['ean'] for c in offers}),3);self.assertEqual(len({c['modelKey'] for c in offers}),1)
  by={c['condition']:c for c in offers}
  self.assertEqual((by['reclaimed']['stock'],by['reclaimed']['price']),('out_of_stock',1.45))
  self.assertEqual((by['mixed']['stock'],by['mixed']['price']),('in_stock',2.65))
  self.assertEqual((by['new']['stock'],by['new']['price']),('orderable',2.99))
  self.assertEqual(by['new']['delivery'],'09-10-2026')
  self.assertNotEqual(by['mixed']['priceTiers'],by['new']['priceTiers'])
 def fixture(self,ean='123',model='X',name='Brand X',stock='Auf Lager',tiers='Kaufen 10 Stück für 2,10 €'):
  return f'''<h1>{name}</h1><table><tr><th>EAN / GTIN</th><td>{ean}</td></tr><tr><th>Marke</th><td>Brand</td></tr><tr><th>Modell</th><td>{model}</td></tr><tr><th>Gewicht - g</th><td>140</td></tr><tr><th>Sicherung</th><td>Ohne</td></tr></table><div class="price-box"><span data-price-amount="5"></span><span class="special-price"><span data-price-amount="3"></span></span></div><ul class="prices-tier"><li>{tiers}</li></ul><span class="stock">{stock}</span><button id="product-addtocart-button">Buy</button>'''
 def test_identity_mismatch_stops_and_preserves_previous(self):
  old={'id':'a','ean':'123','brand':'Brand','model':'X','condition':'new','chargeMax':7};original=copy.deepcopy(old)
  for kwargs in ({'ean':'456'},{'model':'Y'},{'name':'Brand X Reclaimed'}):
   with self.assertRaises(ValueError):product(self.fixture(**kwargs),'https://www.nkon.nl/de/x.html',old)
  self.assertEqual(old,original)
 def test_sale_pack_tiers_and_unknown_stock(self):
  c=product(self.fixture(name='2x Brand X',stock='not available',tiers='Buy 10 pieces for €2.10'),'https://www.nkon.nl/de/2x-x.html',None)
  self.assertEqual(c['pricePack'],3);self.assertEqual(c['price'],1.5);self.assertEqual(c['weight'],70);self.assertEqual(c['priceTiers'],[{'minPacks':10,'pricePack':2.1}]);self.assertEqual(c['stock'],'unknown');self.assertIsNone(c['chargeMax']);self.assertFalse(c['protected'])
 def test_explicit_stock_and_backorder(self):
  for evidence,status in [('Nicht auf Lager','out_of_stock'),('Auf Lager','in_stock'),('09-10-2026','orderable')]:
   self.assertEqual(product(self.fixture(stock=evidence),'https://www.nkon.nl/de/x.html',None)['stock'],status)
 def test_discontinued_overrides_buy_and_stock(self):
  html=self.fixture(stock='Auf Lager')+'<div>Dieses Produkt wurde eingestellt und wird nicht mehr aufgefüllt.</div>'
  c=product(html,'https://www.nkon.nl/de/x.html',None)
  self.assertTrue(c['discontinued']);self.assertEqual(c['stock'],'out_of_stock');self.assertIsNone(c['delivery'])
 def test_lishen_screenshot_correction(self):
  c=next(c for c in self.cells if c['id']=='cell-006')
  self.assertEqual(c['ean'],'6097330531520');self.assertEqual(c['stock'],'out_of_stock');self.assertTrue(c['discontinued']);self.assertEqual(c['shopAuditState'],'visually_checked')
 def test_complete_visual_audit(self):
  import hashlib
  report=json.loads((ROOT/'dist/data/visual-audit.json').read_text());by={r['id']:r for r in report['listings']}
  self.assertEqual(len(by),72)
  for c in self.cells:
   self.assertEqual(c['visualCheck'],'verified');self.assertEqual(c['stock'],by[c['id']]['observed']['stock'])
   self.assertEqual(hashlib.sha256((ROOT/'dist'/c['visualEvidence']).read_bytes()).hexdigest(),c['visualEvidenceSha256'])
  self.assertEqual(sum(c['discontinued'] for c in self.cells),19)
 def test_verified_tiers(self):
  c=next(c for c in self.cells if c['id']=='cell-047');self.assertEqual(c['priceTiers'][0]['pricePack'],5.92)
 def test_tracking_is_not_variant(self):
  self.assertEqual(offer_key('http://nkon.nl/de/x.html?utm_source=test#top'),'https://www.nkon.nl/de/x.html')
  self.assertNotEqual(offer_key('https://nkon.nl/de/x.html?variant=1'),offer_key('https://nkon.nl/de/x.html?variant=2'))
 def test_all_offers_have_auditable_identity(self):
  self.assertEqual(len({c['offerKey'] for c in self.cells}),72)
  for c in self.cells:
   self.assertEqual(c['offerKey'],c['url']);self.assertTrue(c['stockCheckedAt'].startswith('2026-10-01'))
   if c['shopAuditState']=='checked':self.assertTrue(c['ean']);self.assertTrue(c['stockEvidence'])
   elif c['shopAuditState']=='unavailable':self.assertEqual(c['stock'],'unknown')
if __name__=='__main__':unittest.main()
