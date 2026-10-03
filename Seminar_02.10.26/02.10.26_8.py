import random

A = [random.randint(1, 100) for _ in range(43)]
B = [random.randint(1, 100) for _ in range(58)]



print(f"Уникальные значения элементов в каждом множестве:\nA: {" ".join(map(str, list(set(A))))} \nB: {" ".join(map(str, list(set(B))))}")

a = set(A)
b = set(B)

a_b = a.union(b)

print(f"Уникальные для объединения:\nA или B: {" ".join(map(str, list(a_b)))}")

ab = a.intersection(b)

print(f"Уникальные для пересечения:\nA и B: {" ".join(map(str, list(ab)))}")