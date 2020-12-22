import unittest
from mymath.simpleMath import *

class TestSimpleMath(unittest.TestCase):
    def test_add(self):
        z = add(10,20)
        self.assertTrue(z==30)

    def test_sub(self):
        z = sub(20, 10)
        self.assertEqual(z,10)
 