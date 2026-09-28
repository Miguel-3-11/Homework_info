import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

btc = pd.read_csv('BTC_data.csv')
btc['time'] = pd.to_datetime(btc['time'])
btc = btc.sort_values('time').reset_index(drop=True)

fig = plt.figure(figsize=(14, 7))
ax = fig.add_subplot(111)

ax.plot(btc['time'], btc['close'], alpha=0.7)

ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%d-%m-%Y'))
fig.autofmt_xdate()

ax.set_title('Исторический график цены BTC')
ax.set_xlabel('Дата')
ax.set_ylabel('Цена закрытия')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()