class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def isSymmetric(x: Node, y: Node) -> bool:
    if x is None and y is None:
        return True

    A = (x.right is None and y.left is None) or (y.left.key == x.right.key)
    B = (x.left is None and y.right is None) or (y.right.key == x.left.key)

    return (x is not None and y is not None) and \
        (x.key == y.key) and A and B and \
        isSymmetric(x.left, y.right) and isSymmetric(x.right, y.left)


x = Node(15)
x.left = Node(10)
x.right = Node(20)
x.left.left = Node(8)
x.left.right = Node(12)
x.right.left = Node(16)
x.right.right = Node(25)

y = Node(15)
y.left = Node(20)
y.right = Node(10)
y.left.left = Node(25)
y.left.right = Node(16)
y.right.left = Node(12)
y.right.right = Node(8)

print(isSymmetric(x, y))

a = Node(12)
a.left = Node(10)
a.right = Node(2)
a.left.left = Node(1)
a.left.right = Node(13)
a.right.left = Node(16)
a.right.right = Node(24)

b = Node(12)
b.left = Node(10)
b.right = Node(2)
b.left.left = Node(1)
b.left.right = Node(13)
a.right.right = Node(24)

print(isSymmetric(a, b))