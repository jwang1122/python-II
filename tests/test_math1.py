import unittest
from assertFolder.math1 import *

class TestMath1(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3,4), 7)