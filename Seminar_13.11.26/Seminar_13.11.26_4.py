class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self, iterable=()):
        self.head = None
        self.tail = None
        self.size = 0
        for item in iterable:
            self.append(item)

    def __len__(self):
        return self.size

    def __bool__(self):
        return self.size > 0

    def __iter__(self):
        cur = self.head
        while cur is not None:
            yield cur.value
            cur = cur.next

    def __reversed__(self):
        cur = self.tail
        while cur is not None:
            yield cur.value
            cur = cur.prev

    def append(self, value):
        new_node = Node(value, prev=self.tail)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, value):
        new_node = Node(value, next=self.head)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def normalize_index(self, index):
        if index < 0:
            index += self.size
        if not (0 <= index < self.size):
            raise IndexError(f"Индекс {index} вне диапазона [0, {self.size})")
        return index

    def node_at(self, index):
        index = self.normalize_index(index)
        if index < self.size // 2:
            cur = self.head
            for _ in range(index):
                cur = cur.next
        else:
            cur = self.tail
            for _ in range(self.size - 1 - index):
                cur = cur.prev
        return cur

    def insert(self, index, value):
        if index < 0:
            index += self.size
        if index == 0:
            self.prepend(value)
            return
        if index == self.size:
            self.append(value)
            return

        next_node = self.node_at(index)
        prev_node = next_node.prev
        new_node = Node(value, prev=prev_node, next=next_node)
        prev_node.next = new_node
        next_node.prev = new_node
        self.size += 1

    def get(self, index):
        return self.node_at(index).value

    def __getitem__(self, index):
        return self.get(index)

    def remove(self, index):
        node = self.node_at(index)
        prev_node = node.prev
        next_node = node.next

        if prev_node is None:
            self.head = next_node
        else:
            prev_node.next = next_node

        if next_node is None:
            self.tail = prev_node
        else:
            next_node.prev = prev_node

        self.size -= 1
        return node.value

    def pop(self, index=-1):
        return self.remove(index)

    def __repr__(self):
        return "DoublyLinkedList([" + ", ".join(repr(x) for x in self) + "])"

lst = DoublyLinkedList([10, 20, 30, 40, 50])
print("Исходный список :", lst, "  len =", len(lst))

lst.append(60)
lst.prepend(5)
print(lst)

lst.insert(3, 25)
print(lst)

lst.insert(0, 1)
lst.insert(len(lst), 99)
print(lst)

print(lst[-1])
print(lst.get(4))

removed = lst.remove(2)
print(removed, lst)

popped = lst.pop()
print(popped, lst)

print("\nИтерирование в прямом порядке:")

for x in lst:
    print(x, end=" ")

print("\nИтерирование в обратном порядке:")

for x in reversed(lst):
    print(x, end=" ")