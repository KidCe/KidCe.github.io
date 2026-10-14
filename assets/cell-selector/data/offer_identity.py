"""Offer identity: a cell model is a family, each shop listing is independent."""
import re
from urllib.parse import urlsplit,urlunsplit,parse_qsl,urlencode

def offer_key(url):
 p=urlsplit(url)
 if p.hostname not in ('nkon.nl','www.nkon.nl'):raise ValueError('Unexpected offer host')
 query=[(k,v) for k,v in parse_qsl(p.query,keep_blank_values=True) if not k.lower().startswith('utm_') and k not in ('gclid','fbclid')]
 return urlunsplit(('https','www.nkon.nl',p.path,urlencode(sorted(query)),''))
def model_key(brand,model):
 b=re.sub(r'[^a-z0-9]','',(brand or '').lower());m=re.sub(r'[^a-z0-9]','',(model or '').lower())
 if b and m.startswith(b):m=m[len(b):]
 return b+':'+m
def variant_kind(name):
 if re.search(r'reclaimed|renoviert|zurückgefordert',name,re.I):return 'reclaimed'
 if re.search(r'mixed|mischcharge',name,re.I):return 'mixed'
 return 'new'
def attach_identity(c):
 c['offerKey']=offer_key(c['url']);c['modelKey']=model_key(c['brand'],c['model'])
 c['offerVariant']={'reclaimed':'Reclaimed','mixed':'Mixed Batch','new':'Neu / regulär'}[c['condition']]
 return c
def verify_identity(previous,ean,brand,model,name):
 if not previous:return
 if previous.get('ean') and previous['ean']!=ean:raise ValueError('EAN changed: reviewed specifications cannot be inherited')
 if previous.get('model') and model and model_key(previous['brand'],previous['model'])!=model_key(brand,model):raise ValueError('Model changed at offer URL: manual review required')
 if previous.get('condition')!=variant_kind(name):raise ValueError('Offer variant changed: manual review required')
