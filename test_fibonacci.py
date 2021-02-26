import unittest
import fibonacci

class TestCase(unittest.TestCase):

    def test_fib_9(self): # made before the fib() function was created
        self.assertEqual(fibonacci.fib(9), 34)




if __name__ == '__main__':
    unittest.main(verbosity=2)