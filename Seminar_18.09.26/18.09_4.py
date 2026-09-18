def triangle(symb: str, n: int) -> list:
    "Построчно выводит список с рисунком треугольника (рекурсивно)"
    mx_len = n // 2 + 1

    def build(len: int) -> list:
        if len == mx_len:
            return [symb * len] if n % 2 != 0 else []

        rest = build(len + 1)
        curr_str = symb * len
        return [curr_str] + rest + [curr_str]

    return build(0)

n, symb = map(str, input().split())
n = int(n)

print(*triangle(symb, n), sep='\n')