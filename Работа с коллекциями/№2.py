#Задача 1.2 Считать строку с клавиатуры. Используя словарь, посчитать количество уникальных символов

def count_uniqe(text: str) -> dict[str, int]:
    '''Функция считает уникальные символы в словаре'''
    dct = {}

    for item in text:
        dct[item] = dct.get(item, 0) + 1
    return dct


text = input("Введите любой текст: ")
print(count_uniqe(text))
