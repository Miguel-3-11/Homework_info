def decomp(n: int, ans: list) -> list:
    "Рекурсивно раскладывает число на множители"
    primes = eratosphen(n)
    if n == 1:
        return ans
    for p in primes:
        if n % p == 0:
            ans.append(p)
            return decomp(n // p, ans)

def eratosphen(n: int) -> list:
    "Создаёт массив из простых чисел в промежутке от 1 до n"
    res = [i + 1 for i in range(1, n + 1)]
    for i in range(len(res)):
        for j in range(i+1, len(res)):
            if res[i] != 0 and res[j] % res[i] == 0:
                res[j] = 0
    primes = [p for p in res if p != 0]
    return primes

n = int(input())
ans = []
print(f"{n}={'*'.join(map(str, decomp(n, ans)))}")