import unittest
from circle1 import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
# Pathon:Configure Tests
# Pathon:Discover Tests
    def test_area(self):
        self.assertEqual(circle_area(1), pi)
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_area(2.34).__round__(2), 17.20)

    def test_negativeRadius(self):
        self.assertRaises(ValueError, circle_area, -2)

    def test_invalidType(self):
        self.assertRaises(TypeError, circle_area, 3+5j)        
        self.assertRaises(TypeError, circle_area, 'hello')
        self.assertRaises(TypeError, circle_area, None)        
        self.assertRaises(TypeError, circle_area, True)        
        self.assertRaises(TypeError, circle_area, False)