from app.calculator import Calculator
import pytest


class TestCalc:

    def setup(self):
        self.calc = Calculator()

    def test_multiply_correct(self):
        assert self.calc.multiply(10, 2) == 20

    def test_division_correct(self):
        assert self.calc.division(10, 2) == 5.0
        with pytest.raises(ZeroDivisionError) as zero_division:
            self.calc.division(10, 0)

    def test_subtraction_correct(self):
        assert self.calc.subtraction(100, 18) == 82

    def test_adding_correct(self):
        assert self.calc.adding(30, 11) == 41
