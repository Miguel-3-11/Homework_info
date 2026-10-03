from math import pi

r, a = map(int, input().split())

print(f"Длина окружности равна {round(2*pi*r, 2)}.",
    f"\nПлощадь круга составляет {round((pi*r*r)/(a*a)*100, 2)}% от площади квадрата.")