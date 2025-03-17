#Задача 4.1 Создать numpy массив А из случайных чисел размером в 100 элементов.
# Преобразовать его форму в формат 10х10 элементов. Вывести полученный массив.
import numpy as np
import random as rnd


a = np.array([rnd.randrange(1, 100) for _ in range(100)])
a = a.reshape(10, 10)
print(a)
