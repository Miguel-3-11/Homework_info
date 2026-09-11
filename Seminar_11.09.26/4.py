data = list(map(int, input().split()))
for i in range(0, len(data)-1, 2):
  data[i], data[i + 1] = data[i + 1], data[i]
print(*data)