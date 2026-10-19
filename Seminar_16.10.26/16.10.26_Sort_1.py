def is_minheap(arr: list) -> bool:
    ''' Проверяет массив чисел на условие мин кучи, где дети находятся по индексам родителя'''
    n = len(arr)

    for i in range(n // 2):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] > arr[left]:
            return False

        if right < n and arr[i] > arr[right]:
            return False

    return True

arr = list(map(int, input().split()))

print(is_minheap(arr))

