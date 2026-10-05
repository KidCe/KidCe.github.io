"""Historical rebuild must retain all reviewed fields and contradictions."""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]

class SeedReplay(unittest.TestCase):
    def test_rebuilt_seed_equals_reviewed_snapshot(self):
        original = json.loads((ROOT / 'dist/data/cells.json').read_text(encoding='utf-8'))
        with tempfile.TemporaryDirectory(prefix='nkon-seed-test-') as temp:
            target = pathlib.Path(temp)
            shutil.copytree(ROOT / 'scripts', target / 'scripts', ignore=shutil.ignore_patterns('__pycache__'))
            shutil.copytree(ROOT / 'dist/data', target / 'dist/data', ignore=shutil.ignore_patterns('__pycache__'))
            subprocess.run([sys.executable, str(target / 'scripts/build_snapshot.py')], check=True, capture_output=True)
            rebuilt = json.loads((target / 'dist/data/cells.json').read_text(encoding='utf-8'))
            self.assertEqual(original, rebuilt)
            subprocess.run([sys.executable, str(target / 'scripts/audit_snapshot.py')], check=True, capture_output=True)
            self.assertEqual(original, json.loads((target / 'dist/data/cells.json').read_text(encoding='utf-8')))

if __name__ == '__main__':
    unittest.main()
