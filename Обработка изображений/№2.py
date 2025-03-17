#Задача 3.2 Открыть изображение с использованием библиотеки Pillow, отразить изображение слева направо, сохранить результат.

from PIL import Image as img

filename = "images/main_building.jpg"
reversed_filename = "images/reversed_main_building.jpg"
try:
    with open(reversed_filename,'x'):
        with img.open(filename) as image:
            reversed_image = image.transpose(img.FLIP_LEFT_RIGHT)
            reversed_image.save(reversed_filename)
            image.show()
            reversed_image.show()
except FileExistsError:
    print('Файл уже существует, поэтому сохранен не будет.')