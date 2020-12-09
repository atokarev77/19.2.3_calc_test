from app.calculator import Calculator


class TestCalc:

    def setup(self):
        self.calc = Calculator()

    def test_multiply_correct(self):
        assert self.calc.multiply(2, 2) == 4

    def test_multiply_correct(self):
        assert self.calc.multiply(2, 2) == 4
