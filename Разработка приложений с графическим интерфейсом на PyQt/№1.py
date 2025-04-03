#Задача 6.1 Создать дизайн приложения в QtDesigner и сохранить его как ui файл. 
# Подключить дизайн к приложению PyQt и запустить приложение.
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from UI.calculator import Ui_MainWindow

class Calculator(QMainWindow):
    
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = Calculator()
    window.show()
    sys.exit(app.exec())