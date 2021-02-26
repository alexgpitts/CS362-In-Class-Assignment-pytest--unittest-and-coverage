import unittest

import fibonacci



def test_fac_9():
    assert fibonacci.factorial(9) == 362880

def test_fac_0():
    assert fibonacci.factorial(0) == 1 

def test_fac5():
    assert fibonacci.factorial(5) == 120

