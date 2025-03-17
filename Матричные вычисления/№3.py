#Задача 4.3 Создать двухмерный numpy массив А из случайных чисел размером в 100 элементов.
# Выполнить над ним преобразования – транспонирование, сортировку по строкам, сортировку по столбцам, используя методы numpy.
import numpy as np
import random as rnd

matrix = np.array([[rnd.randrange(1, 100) for _ in range(10)] for _ in range(10)])
transposited_matrix = matrix.T
sorted_by_rows_martix = np.sort(matrix, axis=1)
sorted_by_cols_martix = np.sort(matrix, axis=0)


print(f"Сгенерированая матрица: \n {matrix}\n")
print(f"Транспонированная матрица: \n {transposited_matrix}\n")
print(f"Отсортированная по строкам матрица: \n {sorted_by_rows_martix}\n")
print(f"Отсортированная по столбцам матрица: \n {sorted_by_cols_martix}")