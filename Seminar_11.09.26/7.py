data = list(map(str, input().split()))
mx = 0
mx_elem = 0

for elem in data:
  if data.count(elem) > mx:
    mx = data.count(elem)
    mx_elem = elem

print(mx_elem)