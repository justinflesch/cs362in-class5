import calculator


class TestCalculator:

    def test_add(self):
        assert 5 == calculator.add(1, 4)

    def test_sub(self):
        assert 2 == calculator.sub(5, 3)
