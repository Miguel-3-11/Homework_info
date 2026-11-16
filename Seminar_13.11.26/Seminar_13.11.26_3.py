def tokenize_infix(expr: str):
    tokens = []
    i = 0
    expr = expr.replace(' ', '')
    while i < len(expr):
        ch = expr[i]
        if ch.isdigit() or ch == '.':
            j = i
            while j < len(expr) and (expr[j].isdigit() or expr[j] == '.'):
                j += 1
            tokens.append(expr[i:j])
            i = j
        elif ch in ['+', '-', '*', '/', '(', ')', ',']:
            tokens.append(ch)
            i += 1
    return tokens


def sorting_station(expr: str) -> str:
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    left_assoc = {'+', '-', '*', '/'}

    tokens = tokenize_infix(expr)
    output = []
    stack = []

    for tok in tokens:
        if tok.replace('.', '', 1).isdigit():
            output.append(tok)
        elif tok == ',':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
        elif tok in precedence:
            while (stack and stack[-1] in precedence and
                   ((tok in left_assoc and precedence[stack[-1]] >= precedence[tok]))):
                output.append(stack.pop())
            stack.append(tok)
        elif tok == '(':
            stack.append(tok)
        elif tok == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # выбрасываем '('

    while stack:
        op = stack.pop()
        output.append(op)

    return " ".join(output)


expressions = [
    "3 + 4",
    "3 + 4 * 2 / ( 1 - 5 )",
    "(3 + 4 * (2 - 1)) / 5",
    "((2 + 3) * 5 - 1) / 3",
]

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

for e in expressions:
    postfix = sorting_station(e)
    value = stack_calculator(postfix)  # скопипастили функцию из 2го задания
    print(f"Инфиксная: {e}")
    print(f"Постфиксная: {postfix}")
    print(f"Значение: {value}\n")