import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

iris = pd.read_csv('iris_data.csv')

fig = plt.figure(figsize=(12, 5))

ax1 = fig.add_subplot(121)
species_counts = iris['Species'].value_counts()
ax1.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%', startangle=90)
ax1.set_title('Доля разных видов ирисов')

ax2 = fig.add_subplot(122)
bins = [0, 1.2, 1.5, 100]
labels = ['<= 1.2 см', '> 1.2 и <= 1.5 см', '> 1.5 см']
iris['PetalCategory'] = pd.cut(iris['PetalLengthCm'], bins=bins, labels=labels, right=True)
petal_counts = iris['PetalCategory'].value_counts().sort_index()
ax2.pie(petal_counts, labels=petal_counts.index, autopct='%1.1f%%', startangle=90)
ax2.set_title('Доля ирисов по длине лепестка')

plt.tight_layout()
plt.show()