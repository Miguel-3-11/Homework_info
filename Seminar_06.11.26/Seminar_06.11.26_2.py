from math import gcd

def build_tree(a):
    n = len(a)
    tree = {}
    for i in range(n):
        tree[n + i] = a[i]
    for i in range(n - 1, 0, -1):
        tree[i] = gcd(tree[2 * i], tree[2 * i + 1])
    return tree

def gcd_tree(tree, l, r, n):
    d = 0
    l += n
    r += n
    while l < r:
        if (l & 1) > 0:
            d = tree[l]
            l += 1
        if (r & 1) > 0:
            r -= 1
            d = tree[r]
        l = l // 2
        r = r // 2
    return d


n = int(input())
a = list(map(int, input().split()))

tree = build_tree(a)

k = int(input())

for _ in range(k):
    l, r = map(int, input().split())
    print(gcd_tree(tree, l-1, r, n))