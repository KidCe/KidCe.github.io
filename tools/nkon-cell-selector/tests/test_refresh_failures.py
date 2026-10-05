"""Check that blocked and redirected fetches never replace a valid snapshot."""
import json
import pathlib
import sys
import tempfile
import unittest
from unittest.mock import patch, Mock

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'dist/data'))
import update_nkon

class RefreshFailures(unittest.TestCase):
    def test_cloudflare_html_is_not_a_product_or_category(self):
        for blocked in ('Just a moment', 'cf-mitigated', 'verify you are human',
                        'Performing security verification', 'challenges.cloudflare.com'):
            with self.assertRaises(RuntimeError):
                update_nkon.category(blocked, update_nkon.CATEGORY)
            with self.assertRaises(RuntimeError):
                update_nkon.product(blocked, 'https://www.nkon.nl/de/x.html', None)

    def test_failed_refresh_leaves_existing_output_untouched(self):
        snapshot = json.loads((ROOT / 'dist/data/cells.json').read_text(encoding='utf-8'))
        offer = snapshot['cells'][0]['url']
        for mode in ('403', '429', 'redirect', 'blocked_html', 'incomplete'):
            with self.subTest(mode=mode), tempfile.TemporaryDirectory() as tmp:
                src = pathlib.Path(tmp) / 'cells.json'
                src.write_text(json.dumps(snapshot), encoding='utf-8')
                output = pathlib.Path(tmp) / 'new.json'
                output.write_bytes(b'previous-valid-snapshot')
                category = Mock(status_code=200, url=update_nkon.CATEGORY, text='category')
                product = Mock(status_code=200, url=offer, text='Just a moment')
                if mode in ('403', '429'):
                    category.status_code = int(mode)
                if mode == 'redirect':
                    product.url = 'https://www.nkon.nl/de/different-offer.html'
                session = Mock(headers={}, get=Mock(side_effect=[category, product]))
                with patch.object(sys, 'argv', ['update', '--snapshot', str(src), '--output', str(output)]), \
                     patch.object(update_nkon.requests, 'Session', return_value=session), \
                     patch.object(update_nkon.time, 'sleep'), \
                     patch.object(update_nkon, 'category', return_value=([offer], [], 2 if mode == 'incomplete' else 1)):
                    with self.assertRaises((RuntimeError, ValueError)):
                        update_nkon.main()
                self.assertEqual(output.read_bytes(), b'previous-valid-snapshot')
                self.assertEqual(json.loads(src.read_text(encoding='utf-8')), snapshot)
                self.assertFalse(output.with_suffix('.json.tmp').exists())

if __name__ == '__main__':
    unittest.main()
