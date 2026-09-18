import numpy as np

def kramer(matrix_ext: np.array, n: int, m: int) -> list:
    "Решает СЛАУ методом Крамера"

    matrix0 = matrix_ext.copy()
    matrix1 = np.delete(matrix_ext, m - 1, axis = 1)
    det1 = np.linalg.det(matrix1)

    if abs(np.linalg.det(matrix1)) < 1e-6:
        print("Система несовместна")
        return []
    ans = []
    for i in range(m - 1):
        matrix = matrix0.copy()
        matrix[:, i] = matrix[:, m - 1]
        matrix = np.delete(matrix, m - 1, axis = 1)

        x = np.linalg.det(matrix)/det1
        ans.append(float(x))
    return ans


n, m = map(int, input().split())
matrix_ext = np.array([list(map(int, input().split())) for j in range(n)])

print(f"Решение системы: {kramer(matrix_ext, n, m)}")