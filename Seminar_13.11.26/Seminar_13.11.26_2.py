def stack_calculator(expression: str) -> float:
    tokens = expression.split()

    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else (_ for _ in ()).throw(ZeroDivisionError("Деление на ноль")),
    }

    stack = []
    for tok in tokens:
        if tok in ops:
            b = stack.pop()
            a = stack.pop()
            try:
                stack.append(ops[tok](a, b))
            except ZeroDivisionError as e:
                raise ValueError(str(e))
        else:
            try:
                stack.append(float(tok))
            except ValueError:
                raise ValueError(f"Неизвестный токен: '{tok}'")

    result = stack[0]
    return int(result) if result == int(result) else result

tests = [
    "3 4 2 1 - * + 5 /",
    "2 3 + 5 *",
    "10 2 /",
    ]

for expr in tests:
    res = stack_calculator(expr)
    print(f"{expr!r} -> {res}")
