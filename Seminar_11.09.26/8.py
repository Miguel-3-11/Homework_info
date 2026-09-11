N = int(input())
cnt1 = 0
cnt2 = 0
data = list(map(int, input().split()))
for x in data:
    for y in data:
        if x < y:
            cnt1 += 1
        elif x > y:
            cnt2 += 1
    if cnt1 == cnt2:
        print(x)
        break
    cnt1 = 0
    cnt2 = 0
