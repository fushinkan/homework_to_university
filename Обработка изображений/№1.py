#Задача 3.1 Открыть изображение с использованием библиотеки Pillow,
# отобразить в консоль его размер (количество пикселей по ширине и высоте).

from PIL import Image as img

filename = "images/main_building.jpg"
with img.open(filename) as image:
    print(f"Кол-во пикселей по ширине: {image.width}", f"Кол-во пикселей по высоте: {image.height}", sep="\n")