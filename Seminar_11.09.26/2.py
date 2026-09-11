data = list(map(str, input().split()))

N = int(data[0])
old = data[1]
new = ''

for i in range(0, len(old) - N + 1, N):
  s = old[i:i + N]
  new += s[::-1]

print(new)