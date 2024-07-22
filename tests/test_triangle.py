import math
import unittest

from mindbox_area_calculator.calc import Triangle


class TestTriangle(unittest.TestCase):
    """Тесты объектов Triangle."""

    def test_area(self):
        """Тест правильности срассчетов площади треугольника.

        Рассчеты на основе формулы Герона.
        """
        data = [[3, 4, 5], [19.154, 110, 100.56294125]]
        for i in data:
            s1 = i[0]
            s2 = i[1]
            s3 = i[2]
            half_p = (s1 + s2 + s3)/2
            area = math.sqrt(
                half_p * (half_p - s1) * (half_p - s2) * (half_p - s3)
            )
            test_circle = Triangle(*i)
            self.assertEqual(test_circle.area_calc(), area)

    def test_value(self):
        """Тест правильности значений сторон."""
        data = [[3, 4, -5], [19.154, "110", 100.56294125]]
        for i in data:
            with self.assertRaises(ValueError):
                Triangle(*i)

    def test_right_triangle(self):
        """Тест на определение типа треугольника.

        Вычисления происходят по теореме Пифагора.
        Метод возвращает True если треугольник прямоугольный
        и False - если нет.
        """
        data = [[3, 4, 5], [19.154, 110, 100.56294125], [8, 6, 10]]
        for i in data:
            test_triangle = Triangle(*i)
            test_data = sorted(i)
            self.assertEqual(
                test_triangle.is_right_angled(),
                test_data[0]**2 + test_data[1]**2 == test_data[2]**2
            )


if __name__ == "__main__":
    unittest.main()
