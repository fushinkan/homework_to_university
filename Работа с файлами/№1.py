#Задача 2.1 С клавиатуры считать строку А, после чего считать число N. Записать в файл N раз строку А.

def create_file(text: str, count: int = 1, filename = "file.txt") -> None:
    '''Функция считывает строку A и записывает N экземпляров сроки в файл'''
    with open(filename, "w", encoding="utf-8") as file:
        for _ in range(count):
            file.write(text + "\n")

def read_file(filename: str) -> None:
    '''Функция отображает данные из файла'''
    with open(filename, "r", encoding="utf-8") as file:
        data = file.read()
        if not data.strip():
            print("\nОтображение данных в файле:")
            print("Файл пустой")
        else:
            print("\nОтображение данных в файле: ")
            print(data)


#Ввод данных
text = input("Введите любой текст: ")
count = input("Введите кол-во: ")
count = int(count) if count.isdigit() else 1

#Запись в файл
result = create_file(text, count)

#Отображение содержимого в файле
read_file("file.txt")