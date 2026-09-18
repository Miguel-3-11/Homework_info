def gcd_extended(a: int, b: int) -> list:
    "Подсчитывает коэффициенты для диофантова уравнения"
    if b == 0:
        return [1, 0, a]
    x, y, d = gcd_extended(b, a % b)
    x, y = y, x - (a // b) * y
    return [x, y, d]

a, b = map(int, input().split())
print(' '.join(map(str, gcd_extended(a, b))))