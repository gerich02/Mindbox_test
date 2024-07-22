import math
import unittest

from mindbox_area_calculator.calc import Circle


class TestCircle(unittest.TestCase):
    """Тесты объектов Circle."""

    def test_area(self):
        """Тест правильности срассчетов площади круга."""
        data = [3, 4, 15, 19.154, 130, 168.56294125]
        for i in data:
            test_circle = Circle(i)
            self.assertEqual(test_circle.area_calc(), math.pi * i**2)

    def test_value(self):
        """Тест правильности значений радиуса."""
        data = [-0.3, -4, '15', -19.154, 0]
        for i in data:
            with self.assertRaises(ValueError):
                Circle(i)


if __name__ == "__main__":
    unittest.main()
