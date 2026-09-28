import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 0, 15
sample_sizes = [30, 200, 3500]

fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle('Нормальное распределение', fontsize=16)

x_range = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 200)

pdf = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_range - mu) / sigma) ** 2)

for i, size in enumerate(sample_sizes):

    data = np.random.normal(mu, sigma, size)

    axes[i].hist(data, bins=30, density=True, alpha=0.7, label=f'N = {size}')

    axes[i].plot(x_range, pdf, 'r-', linewidth=2, label='Гаусс')

    axes[i].set_title(f'{size} точек')
    axes[i].set_xlabel('Значение')
    axes[i].set_ylabel('Плотность вероятности')
    axes[i].legend()
    axes[i].grid(True, linestyle='--', alpha=0.6)
    axes[i].set_ylim(0, 0.03)
    axes[i].set_xlim(mu - 4 * sigma, mu + 4 * sigma)

plt.show()