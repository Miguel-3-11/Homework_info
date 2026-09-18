import numpy as np

def MNK(x: list, y: list) -> list:
    "Вычисляет коэффициенты полинома первой степени для метода наименьших квадратов"
    x_values = np.array(x)
    y_values = np.array(y)

    return list(np.polyfit(x_values, y_values, 1))


x = list(map(int, input().split()))
y = list(map(int, input().split()))

print(*MNK(x, y))
