class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value   # либо число (float), либо оператор (str)
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None


class Parser:
    def __init__(self, text):
        self.text = text.replace(' ', '')  # убираем пробелы
        self.pos = 0

    def peek(self):
        return self.text[self.pos] if self.pos < len(self.text) else None

    def consume(self, expected=None):
        ch = self.peek()
        self.pos += 1
        return ch

    def parse_number(self):
        start = self.pos
        while self.peek() is not None and (self.peek().isdigit() or self.peek() == '.'):
            self.pos += 1
        return float(self.text[start:self.pos])

    def parse_factor(self):
        ch = self.peek()
        if ch == '(':
            self.consume('(')
            node = self.parse_expr()
            self.consume(')')
            return node
        if ch in '+-':
            op = self.consume()
            operand = self.parse_factor()
            if op == '-':
                return Node('-', Node(0.0), operand)
            return operand
        num = self.parse_number()
        return Node(num)

    def parse_term(self):
        node = self.parse_factor()
        while self.peek() in ['*', '/']:
            op = self.consume()
            right = self.parse_factor()
            node = Node(op, node, right)
        return node

    def parse_expr(self):
        node = self.parse_term()
        while self.peek() in ['+', '-']:
            op = self.consume()
            right = self.parse_term()
            node = Node(op, node, right)
        return node

    def parse(self):
        node = self.parse_expr()
        return node


def to_prefix(node):
    if node.is_leaf():
        v = node.value
        return [str(int(v)) if v == int(v) else str(v)]
    return [node.value] + to_prefix(node.left) + to_prefix(node.right)


def to_postfix(node):
    if node.is_leaf():
        v = node.value
        return [str(int(v)) if v == int(v) else str(v)]
    return to_postfix(node.left) + to_postfix(node.right) + [node.value]

expr = "(3+4*(2-1))/5"
tree = Parser(expr).parse()

print("Исходное выражение :", expr)
print("Прямая польская запись :", " ".join(to_prefix(tree)))
print("Обратная польская запись :", " ".join(to_postfix(tree)))