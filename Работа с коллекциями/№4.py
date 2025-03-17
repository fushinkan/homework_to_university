#Задача 1.4 Написать функцию, принимаю на вход двумерный список с вещественными числами.
# Функция должна возвращать сумму квадратов всех элементов списка.

import random

def create_matrix(left: float = 0.0, right: float = 1.0 , rows: int = 1, cols: int = 1):
    '''Функция создает двумерный список(матрицу)'''
    return [[random.uniform(left, right) for _ in range(cols)] for _ in range(rows)]

def sum_of_matrix(func: callable) -> float:
    '''Функция считает сумму квадратов двумерного спикса(матрицы)'''
    total = 0
    res = func

    for line in res:
        for elem in line:
            total += elem ** 2
    return total


#Ввод и обработка данных
rows = input("Введите кол-во рядов (по умолчанию 1): ")
rows = int(rows) if rows else 1

cols = input("Введите кол-во колонн (по умолчанию 1): ")
cols = int(cols) if cols else 1

left_border = input("\nВведите левую границу случайных чисел (по умолчанию 0.0): ")
left_border = float(left_border) if left_border else 0.0

right_border = input("Введите правую границу случайных чисел (по умолчанию 1.0): ")
right_border = float(left_border) if left_border else 1.0


#Создание матрицы
matrix = create_matrix(left_border, right_border, rows, cols)

#Вывод матрицы
print("\nГенерация матрицы:")
for line in matrix:
    print(*line)

#Вывод результата
result = sum_of_matrix(matrix)
print(f"\nСумма квадратов всех элементов двумерного списка(матрицы) равна {result}")