class Vector:
    def __init__(self, *args):
        self.x, self.y, self.z = map(float, args)

        assert isinstance(self.x, (int, float)) and \
               isinstance(self.y, (int, float)) and \
               isinstance(self.z, (int, float)), "Координаты вектора должны быть числами"

    def __abs__(self):
        """Модуль вектора (длина)"""
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __add__(self, other):
        """Сложение векторов"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        raise TypeError("Можно складывать только с другим объектом класса Vector")

    def __sub__(self, other):
        """Вычитание векторов"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        raise TypeError("Можно вычитать только другой объект класса Vector")

    def __mul__(self, other):
        """Скалярное произведение"""
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        raise TypeError("Умножение возможно на число или на другой объект класса Vector")

    def __rmul__(self, other):
        """Умножение числа на вектор (число * вектор)"""
        return Vector(self.x * other, self.y * other, self.z * other)

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


v1 = Vector(1, 2, 3)
v2 = Vector(10, 3, 6)

print(f"v1: {v1}, v2: {v2}")
print(f"Сложение: {v1 + v2}")
print(f"Вычитание: {v1 - v2}")
print(f"Скалярное произведение: {v1 * v2}")
print(f"Умножение на число 3: {3 * v1}")
print(f"Модуль v1: {abs(v1)}")
print(f"Модуль v2: {abs(v2)}")