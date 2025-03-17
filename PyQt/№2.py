#Задача 5.2 Создать форму с кнопкой и тестовым полем для вывода QLabel.
# При нажатии на кнопку вызывается диалог QMessageBox. Вывести результат (выбранную кнопку в диалоге) в QLabel.
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class MainWindow(QDialog):

    def __init__(self) -> None:

        super().__init__()
        self.setWindowTitle('Нажми на меня_v2.0')  #Создание главного окна и установка его названия

        layout = QVBoxLayout()

        #Создание виджетов


        self.button = QPushButton('Вызвать диалоговое меню', self)
        self.button.clicked.connect(self.click_button)

        self.label = QLabel('Ваш текст будет отображен после завершения работы программы', self)


        #Добавление виджетов на главное окно

        layout.addWidget(self.button)
        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

    def click_button(self) -> None:
        string = 'Сделайте выбор'
        #self.label.setText(string)
        msg = QMessageBox()
        msg.setText(string)
        msg.setStandardButtons(QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Ok)

        res = msg.exec()

        if res == QMessageBox.StandardButton.Ok:
            self.label.setText('Вы нажали Ok')
        else:
            self.label.setText('Вы нажали Cancel')



if __name__ == '__main__':
    app = QApplication(sys.argv) #Создает приложение
    main_window = MainWindow() #Создает главное окно для приложения
    main_window.show()
    main_window.resize(500, 400)
    sys.exit(app.exec())
