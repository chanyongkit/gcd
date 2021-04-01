import unittest
import gcd

class TestGcd(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd.gcd(0,5), 0)
        self.assertEqual(gcd.gcd(5,0), 0)
        self.assertEqual(gcd.gcd(0,0), 0)
        self.assertEqual(gcd.gcd('str','string'), -1)
        self.assertEqual(gcd.gcd('str',3), -1)
        self.assertEqual(gcd.gcd(3,'str'), -1)
        self.assertEqual(gcd.gcd(5,1845), 5)
        self.assertEqual(gcd.gcd(1845,5), 5)
        self.assertEqual(gcd.gcd(500,500), 500)
        self.assertEqual(gcd.gcd(250,5), 5)
        self.assertEqual(gcd.gcd(18,24), 6)
        self.assertEqual(gcd.gcd(gcd.gcd(36,48), 210),6)


if __name__ == '__main__':
    unittest.main()