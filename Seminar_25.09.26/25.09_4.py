import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

iris = pd.read_csv('iris_data.csv')

combinations = [
    ('SepalLengthCm', 'SepalWidthCm'),
    ('SepalLengthCm', 'PetalLengthCm'),
    ('SepalLengthCm', 'PetalWidthCm'),
    ('SepalWidthCm', 'PetalLengthCm'),
    ('SepalWidthCm', 'PetalWidthCm'),
    ('PetalLengthCm', 'PetalWidthCm')
]

fig = plt.figure(figsize=(15, 10))

colors = {'Iris-setosa': 'blue', 'Iris-versicolor': 'green', 'Iris-virginica': 'red'}

best_r2 = -1
best_combo = None
best_coeffs = None

for i, (x_feat, y_feat) in enumerate(combinations):
    ax = fig.add_subplot(2, 3, i + 1)
    for species, color in colors.items():
        subset = iris[iris['Species'] == species]
        ax.scatter(subset[x_feat], subset[y_feat], color=color, label=species, alpha=0.7)

    x = iris[x_feat].values
    y = iris[y_feat].values
    coeffs = np.polyfit(x, y, 1)
    p = np.poly1d(coeffs)

    x_line = np.linspace(x.min(), x.max(), 100)
    y_line = p(x_line)
    ax.plot(x_line, y_line, color='black', linestyle='--', linewidth=2)

    ax.set_title(f'{y_feat} vs {x_feat}')
    ax.set_xlabel(x_feat)
    ax.set_ylabel(y_feat)

    ss_res = np.sum((y - p(x)) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r2 = 1 - (ss_res / ss_tot)

    if r2 > best_r2:
        best_r2 = r2
        best_combo = (x_feat, y_feat)
        best_coeffs = coeffs

ax.legend(title='Species')
plt.tight_layout()
plt.show()

print(f"Лучшая зависимость: {best_combo[1]} от {best_combo[0]}")
print(f"R^2: {best_r2:.4f}")
print(f"Уравнение: {best_combo[1]} = {best_coeffs[0]:.4f} * {best_combo[0]} + {best_coeffs[1]:.4f}")