data = list(map(int, input().split()))
N = data.pop(0)

print((N * (N + 1)) // 2 - sum(data))