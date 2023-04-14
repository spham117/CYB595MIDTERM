from unittest import TestCase

from main import addition, subtraction, multiplication, division


class Test(TestCase):
    def test_addition(self):
        assert addition(2, 3) == 5
    def test_subtraction(self):
        assert subtraction(2, 3) == -1
    def test_multiplication(self):
        assert multiplication(2, 3) == 6
    def test_division(self):
        assert division(6, 3) == 2
