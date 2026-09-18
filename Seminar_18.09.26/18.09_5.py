import numpy as np

def spiral(n: int, m: int) -> np.array:
    "Создаёт матрицу NxM, заполненную спиралью по часовой стрелке."
    matrix = np.zeros((n, m), dtype=int)

    t = 0
    b = n - 1
    l = 0
    r = m - 1
    num = 1

    while t <= b and l <= r:
        for i in range(l, r + 1):
            matrix[t, i] = num
            num += 1
        t += 1

        for i in range(t, b + 1):
            matrix[i, r] = num
            num += 1
        r -= 1

        if t <= b:
            for i in range(r, l - 1, -1):
                matrix[b, i] = num
                num += 1
            b -= 1

        if l <= r:
            for i in range(b, t - 1, -1):
                matrix[i, l] = num
                num += 1
            l += 1

    return matrix


n, m = map(int, input().split())
matrix = spiral(n, m)
multipliers = np.arange(1, n + 1).reshape(n, 1)
result = matrix * multipliers

for row in result:
    print(*row)