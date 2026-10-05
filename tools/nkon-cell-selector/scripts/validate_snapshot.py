"""Validate a snapshot and any claimed visual evidence without network requests."""
import argparse
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'dist/data'))
from offer_identity import offer_key

def validate(path):
    snapshot = json.loads(path.read_text(encoding='utf-8'))
    cells = snapshot['cells']
    assert snapshot['schemaVersion'] == 1 and cells
    assert snapshot['completeCatalog'] and snapshot['expectedCount'] == len(cells)
    assert len({c['id'] for c in cells}) == len(cells), 'Duplicate IDs'
    assert len({offer_key(c['url']) for c in cells}) == len(cells), 'Duplicate offers'
    for c in cells:
        assert c['stock'] in ('in_stock', 'orderable', 'out_of_stock', 'unknown')
        assert not c.get('discontinued') or c['stock'] == 'out_of_stock'
        assert c['offerKey'] == offer_key(c['url'])
        assert isinstance(c['sources'], list) and isinstance(c['notes'], list)
        for key in ('capacity', 'chargeStandard', 'chargeMax', 'chargeFast',
                    'dischargeShop', 'dischargeSheet', 'weight', 'price'):
            v = c.get(key)
            assert v is None or isinstance(v, (int, float)) and v >= 0, (c['id'], key)
        if c.get('visualCheck') == 'verified':
            evidence = (path.parent.parent / c['visualEvidence']).resolve()
            assert evidence.is_relative_to(path.parent.resolve()), 'Evidence path outside data'
            assert hashlib.sha256(evidence.read_bytes()).hexdigest() == c['visualEvidenceSha256']
    if (snapshot.get('visualAuditSummary') or {}).get('complete'):
        report = json.loads((path.parent / 'visual-audit.json').read_text(encoding='utf-8'))
        assert {r['id'] for r in report['listings']} == {c['id'] for c in cells}
        assert all(c.get('visualCheck') == 'verified' for c in cells)
    print(f'Validated {len(cells)} exact offers, dated {snapshot["snapshotDate"]}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--snapshot', type=pathlib.Path, default=ROOT / 'dist/data/cells.json')
    validate(parser.parse_args().snapshot)
