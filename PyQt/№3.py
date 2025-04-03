#Задача 5.3 Создать форму с различными графическими элементами:
# QCheckBox, QRadioButton, QSlider и отобразить в консоль их текущее состоянии при взаимодействии с ними (нажатии).
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QRadioButton, QSlider
from PyQt6.QtCore import Qt



class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Выбери")
        
        layout = QVBoxLayout()
        
        
        #Чекбокс
        self.checkbox = QCheckBox("Чекбокс")
        self.checkbox.stateChanged.connect(self.checkbox_state)

        
        #Радио-кнопка
        self.radio_button = QRadioButton("Радио-кнопка")
        self.radio_button.toggled.connect(self.radio_button_state)
        
        
        #Слайдер
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 50)
        self.slider.valueChanged.connect(self.slider_state)
        
        
        #Добавление виджетов в окружение
        layout.addWidget(self.checkbox)
        layout.addWidget(self.radio_button)
        layout.addWidget(self.slider)
        self.setLayout(layout)
        
        
    #Подключение состоянийй кнопок
    def checkbox_state(self, state):
        print(f"Чекбокс: {'Включен' if state == 2 else 'Выключен'}")
        
    def radio_button_state(self, state):
        print(f"Радио-кнопка: {'Включена' if state == 1 else 'Выключена'}")
        
    def slider_state(self, value):
        print(f"Слайдер: {value}")
        
        
            

if __name__ == '__main__':
    app = QApplication(sys.argv) #Создает приложение
    main_window = MainWindow() #Создает главное окно для приложения
    main_window.show()
    main_window.resize(500, 400)
    sys.exit(app.exec())