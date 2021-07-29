"""
Unit tests for the calculator library
"""
import math

import pytest

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)
        assert math.isclose(1 - 0.99, 0.01)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)

    def test_division(self):
        assert 2 == calculator.divide(8, 4)
        assert calculator.divide(4.5, 2.25) == 2.0
        with pytest.raises(ZeroDivisionError):
            calculator.divide(1, 0)
