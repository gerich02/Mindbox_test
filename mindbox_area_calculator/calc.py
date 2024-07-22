import math
from abc import ABC, abstractmethod


class Figure(ABC):
    """Абстрактный базовый класс для фигур."""

    @abstractmethod
    def area_calc(self):
        """Метод для расчета площади.

        Обязательно должен быть переопределен в подклассах.
        """
        pass


class Circle(Figure):
    """Класс, для создания экземпляра круга."""

    def __init__(self, radius: float):
        super().__init__()
        if not self.is_valid_circle(radius):
            raise ValueError("Круга с таким радиусом не может существовать")
        self.radius = radius

    def is_valid_circle(self, r: float):
        """Проверка, может ли треугольник с такими сторонами существовать."""
        return r > 0

    def area_calc(self):
        """Метод, для рассчета площади круга."""
        area = math.pi * self.radius**2
        print(f'Площадь круга с радиусом {self.radius} равна {area}')


class Triangle(Figure):
    """Класс, для создания экземпляра треугольника."""

    def __init__(self,  side1: float, side2: float, side3: float):
        super().__init__()
        if not self.is_valid_triangle(side1, side2, side3):
            raise ValueError(
                "Треугольник с такими сторонами не может существовать"
            )
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def is_valid_triangle(self, s1: float, s2: float, s3: float):
        """Проверка, может ли треугольник с такими сторонами существовать."""
        if s1 > 0 and s2 > 0 and s3 > 0:
            return (s1 + s2 > s3) and (s1 + s3 > s2) and (s2 + s3 > s1)
        return False

    def area_calc(self):
        """Метод, для рассчета площади треугольника по формуле Герона."""
        s1 = self.side1
        s2 = self.side2
        s3 = self.side3
        half_p = (s1 + s2 + s3)/2
        area = math.sqrt(
            half_p * (half_p - s1) * (half_p - s2) * (half_p - s3)
        )
        print(f'Площадь треугольника со сторонами {self.side1}, {self.side2}'
              f' и {self.side3} равна {area}')

    def is_right_angled(self):
        """Метод, определяющий является ли треугольник прямоугольным."""
        side_list = sorted([self.side1, self.side2, self.side3])
        if side_list[0]**2 + side_list[1]**2 == side_list[2]**2:
            print(f'Треугольник со сторонами {self.side1}, {self.side2}'
                  f' и {self.side3} прямоугольный')
        else:
            print(f'Треугольник со сторонами {self.side1}, {self.side2}'
                  f' и {self.side3} не прямоугольный')


Circle1 = Circle(0.5)
Circle1.area_calc()

Triangle1 = Triangle(8, 6, 11)
Triangle1.area_calc()
Triangle1.is_right_angled()
