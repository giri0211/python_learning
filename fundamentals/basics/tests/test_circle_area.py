from math import pi
from fundamentals.basics.unit_tests.circle_area import calc_cricle_area
import unittest

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # test areas
        self.assertAlmostEqual(calc_cricle_area(1), pi)
        self.assertAlmostEqual(calc_cricle_area(0), 0)
        self.assertAlmostEqual(calc_cricle_area(2.1), pi*2.1**2)
        
    def test_values(self):
        self.assertRaises(ValueError, calc_cricle_area, -2)
    
    def test_type(self):
        self.assertRaises(TypeError, calc_cricle_area, 3+5j)
        self.assertRaises(TypeError, calc_cricle_area, True)
        self.assertRaises(TypeError, calc_cricle_area, "radius")