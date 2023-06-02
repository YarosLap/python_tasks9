# Создайте двумерный массив случайного размера.
# Найдите индексы максимального и минимального элементов в нём.
# Выведите элементы главной диагонали матрицы в виде одномерного массива.

import numpy as np

size = np.random.randint(3, 10)

a = np.random.randint(0, 10, (size, size))
print(a)

min_index = np.unravel_index(a.argmin(), a.shape)
max_index = np.unravel_index(a.argmax(), a.shape)

print(f'Индексы минимального элемента: {min_index}')
print(f'Индексы максимального элемента: {max_index}')

diag_arr = np.diag(a)
print(f'Элементы главной диагонали матрицы: {diag_arr}')
