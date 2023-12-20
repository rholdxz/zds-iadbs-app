"""
How to make Test of Calc.py
"""
from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """Class Calculate Test Sample."""

    def test_add_number(self):
        """Test function adding numbers."""
        res = calc.add(5, 5)
        self.assertEqual(res, 10, msg="The sum is not correct")
