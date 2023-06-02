# Дан список элементов. Используя библиотеку NumPy, подсчитайте количество уникальных элементов в нём.

import numpy as np

array = np.array([1,1,1,2,3,4,4,4])

unique, counts = np.unique(array, return_counts=True)

result = np.column_stack((unique, counts))
print (result)
