#Задача 5.1 Создать окно с одной кнопкой QPushButton, полем для ввода QLineEdit и тестовым полем для вывода QLabel.
# При нажатии на QPushButton считать данные из QLineEdit и вывести их в QLabel.
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class MainWindow(QDialog):

    def __init__(self) -> None:

        super().__init__()
        self.setWindowTitle('Нажми на меня')  #Создание главного окна и установка его названия

        layout = QVBoxLayout()

        #Создание виджетов
        self.line = QLineEdit(self)
        self.line.setPlaceholderText('Напишите что то...')

        self.button = QPushButton('Подтвердить', self)
        self.button.clicked.connect(self.click_button)

        self.label = QLabel('Ваш текст будет отображен здесь.', self)


        #Добавление виджетов на главное окно
        layout.addWidget(self.line)
        layout.addWidget(self.button)
        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

    def click_button(self) -> None:
        string = self.line.text()
        self.label.setText(string)



if __name__ == '__main__':
    app = QApplication(sys.argv) #Создает приложение
    main_window = MainWindow() #Создает главное окно для приложения
    main_window.show()
    main_window.resize(500, 400)
    sys.exit(app.exec())
