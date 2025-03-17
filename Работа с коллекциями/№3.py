#Задача 1.3 Написать функцию, принимаю на вход строку. Функция должна возвращать строку с удалёнными знаками препинания
import string
from string import punctuation

def del_puntcuation(text: str) -> str:
    '''Функция удаляет знаки препинания в тексте'''
    for chr in text:
        if chr in string.punctuation:
            text = text.replace(chr, '')
    return text


text = input("Введите текс со знаками пренинания: ")
print(del_puntcuation(text))