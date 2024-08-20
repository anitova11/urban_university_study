from math import pi


class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled=False):
        self.__color = color
        self.filled = filled
        self.__sides = []
        self.set_sides(*sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if all((0 <= i <= 255) & isinstance(i, int) for i in (r, g, b)):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b

    def __is_valid_sides(self, *sides):
        if len(sides) == self.sides_count:
            for i in sides:
                if i > 0 and isinstance(i, int):
                    continue
                else:
                    return False
            return True
        else:
            return False

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = [*sides]
        elif len(sides) == 1 and self.sides_count == 12 and sides[0] > 0:
            self.__sides = []
            for i in range(12):
                self.__sides.append(*sides)
        elif self.__sides != []:
            pass
        else:
            self.__sides = []
            for i in range(self.sides_count):
                self.__sides.append(1)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        summa = 0
        for i in self.__sides:
            summa += i
        return summa


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *side):
        super().__init__(color, *side)
        self.__radius = (self._Figure__sides[0] / 2) / pi

    def get_square(self):
        return self.__radius ** 2 * pi


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = 2 * self.get_square() / self._Figure__sides[0]  # нахожу высоту, проведенную к 1ой стороне
        print(self.__height)

    def get_square(self):
        p = len(self) / 2
        mul = 1
        for i in self._Figure__sides:
            mul *= p - i
        return (p * mul) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *side):
        super().__init__(color, *side)

    def get_volume(self):
        return self._Figure__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
cube1.set_color(300, 70, 15) # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
circle1.set_sides(15) # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
