#Задача 4.2 Создать два двухмерных numpy массива А и В, заполнить из случайными числами от 1 до 100.
# Вывести результат А+В, А-В, А**2, А+100.

import numpy as np
import random as rnd

n = int(input("Введите размерность массивов: "))

a = np.array([[rnd.randrange(1, 100) for _ in range(n)] for _ in range(n)])
b = np.array([[rnd.randrange(1, 100) for _ in range(n)] for _ in range(n)])


print(f"Массив А:\n {a}\n")
print(f"Массив B:\n {b}\n")
print(f"A+B:\n {a + b}\n")
print(f"A-B:\n {a - b}")
print(f"A**2:\n {a **2}\n")
print(f"A+100:\n {a + 100}")