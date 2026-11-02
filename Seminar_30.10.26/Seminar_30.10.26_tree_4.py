class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def Symmetrate(x: Node) -> None:
    if x is None:
        return

    if x.right is not None or x.left is not None:
        x.right, x.left = x.left, x.right
        Symmetrate(x.left)
        Symmetrate(x.right)

x = Node(15)
x.left = Node(10)
x.right = Node(20)
x.left.left = Node(8)
x.left.right = Node(12)
x.right.left = Node(16)
x.right.right = Node(25)

Symmetrate(x)

print(x.key)
print(x.left.key)
print(x.right.key)
print(x.left.left.key)
print(x.left.right.key)
print(x.right.left.key)
print(x.right.right.key)

# Я проверял, код работает и с незаполненными деревьями, но это менее красиво, поэтому для примера полность заполненное дерево