class Node:
    def __init__(self, key=None, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

def create_path(x):
    path = []
    while x.parent is not None:
        path.append(x.parent.key)
        x = x.parent
    return path

def dfs(x, v):
    if x is None or x.key == v:
        return []

    stack = [x]

    while stack:
        node = stack.pop()

        if node.right:
            stack.append(node.right)
            if node.right.key == v:
                return create_path(node.right)

        if node.left:
            stack.append(node.left)
            if node.left.key == v:

                return create_path(node.left)

x = Node(15)
x.left = Node(10)
x.right = Node(20)
x.left.left = Node(8)
x.left.right = Node(12)
x.right.parent = Node(15)
x.right.left = Node(16)
x.right.right = Node(25)

# Инициализируем предков
x.left.parent = x
x.right.parent = x
x.left.left.parent = x.left
x.left.right.parent = x.left
x.right.left.parent = x.right
x.right.right.parent = x.right

v = int(input())

if dfs(x, v) is not None:
    print("Путь до корня:", v, *dfs(x, v))
elif dfs(x, v) == [x.key]:
    print("Искомая вершина - корень")
else:
    print("Искомой вершины нет в дереве")