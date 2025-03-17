#Задача 1.1 Считать строку с клавиатуры, состоящую из чисел через пробел. Преобразовать строку с список целых чисел.

def str_to_int(text: str) -> list[int]:
    for chr in text:
        if chr.isalpha():
            raise TypeError("Строка должна состоять только из цифр!")
    return [int(i) for i in text.split()]


text = input("Введите строку, состоящую из цифр: ")
print(str_to_int(text))
