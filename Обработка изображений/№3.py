#Задача 3.3 Открыть изображение с использованием библиотеки Pillow,
# сделать негатив изображения (отразить значения цветов пикселей), сохранить результат.
from PIL import Image, ImageOps

filename = "images/main_building.jpg"
negative_filename = "images/negative_main_building.jpg"
try:
    with open(negative_filename, 'x'):
        with Image.open(filename, 'r') as img:
            negative_img = ImageOps.invert(img)
            negative_img.save(negative_filename)
            img.show()
            negative_img.show()
except FileExistsError:
    print('Файл уже существует, поэтому сохранен не будет.')