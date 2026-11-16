import unittest
import os
import glob
from vulnerable_sql import get_user_vulnerable
from secure_sql import get_user_secure
from trojan_calculator import TrojanCalculator
from custom_hash import compare_hashes
import worm

class TestSecurityHw(unittest.TestCase):
    def test_vulnerable_sql(self):
        # test Mock DB with SQL injection
        result = get_user_vulnerable("1' OR '1'='1")
        self.assertTrue(len(result) == 2)

    def test_secure_sql(self):
        result = get_user_secure("1' OR '1'='1")
        self.assertEqual(len(result), 0)

    def test_trojan(self):
        calc = TrojanCalculator()
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(4, 6), 10)
        self.assertEqual(calc.add(1, 1), 10)

    def test_worm(self):
        worm.spread_worm()
        copies = glob.glob('worm_*.py')
        self.assertTrue(len(copies) <= 5)
        for f in copies:
            os.remove(f)

    def test_hash(self):
        self.assertTrue(compare_hashes("cyber", "cyber"))
        self.assertFalse(compare_hashes("cyber", "security"))

if __name__ == '__main__':
    unittest.main()