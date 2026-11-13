import unittest,json,re
from pathlib import Path
ROOT=Path(__file__).parents[1]
class LibraryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.entries=json.loads((ROOT/'prompts/system_prompts.json').read_text())["entries"]
    def test_catalog_unique_and_complete(self):
        self.assertEqual(len(self.entries),36)
        self.assertEqual(len({e['id'] for e in self.entries}),36)
        self.assertEqual(len({e['category'] for e in self.entries}),10)
    def test_version_and_grounding_contract(self):
        for e in self.entries:
            with self.subTest(prompt=e['id']):
                self.assertRegex(e['version'],r'^\d+\.\d+\.\d+$')
                self.assertIn('untrusted data',e['system'])
                self.assertIn('required JSON',e['system'])
                self.assertTrue(e['focus'])
    def test_extraction_examples_are_grounded(self):
        for e in self.entries:
            if e['category']!='extraction':continue
            for example in e['few_shot']:
                out=example['output'];self.assertIn(out['evidence_quote'],example['source'])
                self.assertIn(out['property_name'],example['source'])
                for field in ('area_sqm','total_price_rub'):
                    if out[field] is not None:self.assertIn(str(out[field]),example['source'])
