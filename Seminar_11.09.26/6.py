data = list(map(str, input().split()))
for elem in data:
  if data.count(elem) == 1:
    print(elem)