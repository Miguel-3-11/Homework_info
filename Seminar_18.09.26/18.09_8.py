import numpy as np
import random

def MNK(x: list, y: list) -> list:
    "Вычисляет коэффициенты полинома первой степени для метода наименьших квадратов с рандомными данными с заданными параматреами распределений"
    x_values = np.array(x)
    y_values = np.array(y)

    return list(np.polyfit(x_values, y_values, 1))

n = int(input())
x = [random.uniform(0.0, 10.0) for _ in range(n)]
y = [random.gauss(10.0, 7.0) for _ in range(n)]

print(*MNK(x, y))
