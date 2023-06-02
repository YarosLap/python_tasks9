# Создайте двумерный массив, размером 5х5. Определите, есть ли в нём одинаковые строки.

import numpy as np

arr = np.random.randint(0, 2, (5, 5))
print(arr)

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if (arr[i] == arr[j]).all():
            print('Одинаковые строки есть')
            break
    else:
        continue
    break
else:
    print('Одинаковых строк нет')


