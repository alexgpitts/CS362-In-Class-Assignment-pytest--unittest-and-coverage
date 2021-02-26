import unittest

import fibonacci


#unittest class tests
class TestCase(unittest.TestCase):
    def test_fac_9(self):
        self.assertEqual(fibonacci.factorial(9), 362880) 
    def test_fac_0(self): 
        self.assertEqual(fibonacci.factorial(0), 1)
    def test_fac5(self): 
        self.assertEqual(fibonacci.factorial(5), 120)    



if __name__ == '__main__':
    unittest.main(verbosity=2)