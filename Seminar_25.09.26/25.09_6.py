import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

btc = pd.read_csv('BTC_data.csv')
btc['time'] = pd.to_datetime(btc['time'])
btc = btc.sort_values('time').reset_index(drop=True)
btc['time_index'] = np.arange(len(btc))

fig = plt.figure(figsize=(14, 7))
ax = fig.add_subplot(111)

ax.plot(btc['time'], btc['close'], label='BTC Close Price', alpha=0.6, linewidth=1)

ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%d-%m-%Y'))
fig.autofmt_xdate()

coeffs = np.polyfit(btc['time_index'], btc['close'], 3)
poly_fn = np.poly1d(coeffs)
btc['poly_fit'] = poly_fn(btc['time_index'])

ax.plot(btc['time'], btc['poly_fit'], color='red', label='Polynomial Fit (x^3)', linewidth=2)

ax.set_title('Исторический график цены BTC с полиномиальной аппроксимацией')
ax.set_xlabel('Дата')
ax.set_ylabel('Цена закрытия')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print(f"Коэффициенты полинома:")
print(f"P(x) = {coeffs[0]:.4e} * x^3 + {coeffs[1]:.4e} * x^2 + {coeffs[2]:.4e} * x + {coeffs[3]:.4e}")