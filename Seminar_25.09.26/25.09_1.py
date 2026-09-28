import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

U1 = [544, 504, 360, 340, 308, 280, 220, 160, 140, 120]
I1 = [268.35, 247.71, 177.37, 167.40, 150.68, 136.20, 107.61, 78.81, 69.24, 59.10]

U2 = [592, 536, 496, 452, 428, 400, 376, 300, 232, 208]
I2 = [196.57, 177.78, 163.76, 150.47, 142.20, 131.75, 124.12, 99.56, 77.56, 68.74]

U3 = [568, 520, 480, 464, 440, 400, 380, 296, 336, 360]
I3 = [112.48, 103.23, 94.77, 91.74, 87.53, 78.92, 75.21, 59.11, 66.51, 70.90]

datasets = [
    ("l = 20,2 cm", I1, U1),
    ("l = 30,1 cm", I2, U2),
    ("l = 50,0 cm", I3, U3)
]

plt.figure(figsize=(10, 7))


for name, I, U in datasets:
    I_arr = np.array(I)
    U_arr = np.array(U)

    R_avg = np.mean(U_arr / I_arr)
    slope, intercept, r_value, p_value, std_err = linregress(I_arr, U_arr)

    plt.scatter(I_arr, U_arr, label=f'{name}', alpha=0.7, s=20, zorder=3)

    I_fit = np.linspace(0, max(I_arr), 100)
    U_fit = slope * I_fit + intercept
    plt.plot(I_fit, U_fit, linewidth=2, zorder=2)

plt.title('Зависимость напряжения от тока', fontsize=14)
plt.xlabel('I, mA', fontsize=12)
plt.ylabel('U, mV', fontsize=12)

plt.xlim(left=0)
plt.ylim(bottom=0)

plt.legend(loc='upper left')
plt.grid(True, linestyle='--', alpha=0.7, zorder=1)
plt.tight_layout()

plt.show()
