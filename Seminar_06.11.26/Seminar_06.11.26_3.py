def build_tree(a):
    n = len(a)
    tree = {}
    for i in range(n):
        tree[n + i] = 0 if a[i] else 1
    for i in range(n - 1, 0, -1):
        tree[i] = tree[2 * i] + tree[2 * i + 1]
    return tree


def zero_tree(tree, l, r, k, n):
    zeros = 0
    l += n
    r += n
    while l < r:
        if (l & 1) > 0:
            zeros += tree[l]
            l += 1
        if (r & 1) > 0:
            r -= 1
            zeros += tree[r]
        l //= 2
        r //= 2

    if zeros < k:
        return -1

    left = l
    right = r - 1
    idx = -1

    while left <= right:
        mid = (left + right) // 2

        zeros_cnt = 0
        l = l + n
        r = mid + 1 + n
        while l < r:
            if l & 1:
                zeros_cnt += tree[l]
                l += 1
            if r & 1:
                r -= 1
                zeros_cnt += tree[r]
            l //= 2
            r //= 2

        if zeros_cnt >= k:
            idx = mid
            right = mid - 1
        else:
            left = mid + 1

    return idx + 1


n = int(input())
a = list(map(int, input().split()))

tree = build_tree(a)

k = int(input())

for _ in range(k):
    l, r, k = map(int, input().split())
    print(zero_tree(tree, l-1, r, k, n))