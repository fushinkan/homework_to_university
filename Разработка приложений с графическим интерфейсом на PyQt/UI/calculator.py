# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import file_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 640)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icons/calculate_24dp_121212_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(480, 640))
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"	background-color: #121212;\n"
"	font-family: Rubik;\n"
"	color: white;\n"
"	font-weight: 600;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #888;\n"
"}\n"
"\n"
"QLabel {\n"
"	font-size: 40pt;\n"
"	font-weight: 600;\n"
"	color: #888\n"
"}\n"
"\n"
"QLineEdit {\n"
"	font-size: 40pt;\n"
"	font-weight: 600;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_temp = QLabel(self.centralwidget)
        self.lbl_temp.setObjectName(u"lbl_temp")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lbl_temp.sizePolicy().hasHeightForWidth())
        self.lbl_temp.setSizePolicy(sizePolicy2)
        self.lbl_temp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.lbl_temp)

        self.le_entry = QLineEdit(self.centralwidget)
        self.le_entry.setObjectName(u"le_entry")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.le_entry.sizePolicy().hasHeightForWidth())
        self.le_entry.setSizePolicy(sizePolicy3)
        self.le_entry.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.le_entry.setReadOnly(True)

        self.verticalLayout.addWidget(self.le_entry)

        self.layout = QGridLayout()
        self.layout.setObjectName(u"layout")
        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy4)
        font = QFont()
        font.setFamilies([u"Rubik"])
        font.setPointSize(18)
        font.setBold(True)
        self.btn_3.setFont(font)
        self.btn_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_3.setIconSize(QSize(16, 16))

        self.layout.addWidget(self.btn_3, 3, 2, 1, 1)

        self.btn_point = QPushButton(self.centralwidget)
        self.btn_point.setObjectName(u"btn_point")
        sizePolicy4.setHeightForWidth(self.btn_point.sizePolicy().hasHeightForWidth())
        self.btn_point.setSizePolicy(sizePolicy4)
        self.btn_point.setFont(font)
        self.btn_point.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_point.setIconSize(QSize(16, 16))

        self.layout.addWidget(self.btn_point, 4, 2, 1, 1)

        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy4.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy4)
        self.btn_clear.setFont(font)
        self.btn_clear.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_clear.setIconSize(QSize(16, 16))

        self.layout.addWidget(self.btn_clear, 0, 0, 1, 1)

        self.btn_clear_entry = QPushButton(self.centralwidget)
        self.btn_clear_entry.setObjectName(u"btn_clear_entry")
        sizePolicy4.setHeightForWidth(self.btn_clear_entry.sizePolicy().hasHeightForWidth())
        self.btn_clear_entry.setSizePolicy(sizePolicy4)
        self.btn_clear_entry.setFont(font)
        self.btn_clear_entry.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_clear_entry.setIconSize(QSize(16, 16))

        self.layout.addWidget(self.btn_clear_entry, 0, 1, 1, 1)

        self.btn_backspace = QPushButton(self.centralwidget)
        self.btn_backspace.setObjectName(u"btn_backspace")
        sizePolicy4.setHeightForWidth(self.btn_backspace.sizePolicy().hasHeightForWidth())
        self.btn_backspace.setSizePolicy(sizePolicy4)
        self.btn_backspace.setFont(font)
        self.btn_backspace.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/backspace_24dp_FFF_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_backspace.setIcon(icon1)
        self.btn_backspace.setIconSize(QSize(16, 16))

        self.layout.addWidget(self.btn_backspace, 0, 2, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy4.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy4)
        self.btn_8.setFont(font)
        self.btn_8.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_8.setIconSize(QSize(16, 16))

        self.layout.addWidget(self.btn_8, 1, 1, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy4.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy4)
        self.btn_7.setFont(font)
        self.btn_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_7.setIconSize(QSize(16, 16))

        self.layout.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_eq = QPushButton(self.centralwidget)
        self.btn_eq.setObjectName(u"btn_eq")
        sizePolicy4.setHeightForWidth(self.btn_eq.sizePolicy().hasHeightForWidth())
        self.btn_eq.setSizePolicy(sizePolicy4)
        self.btn_eq.setFont(font)
        self.btn_eq.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_eq.setIconSize(QSize(16, 16))

        self.layout.addWidget(self.btn_eq, 4, 3, 1, 1)

        self.btn_prod = QPushButton(self.centralwidget)
        self.btn_prod.setObjectName(u"btn_prod")
        sizePolicy4.setHeightForWidth(self.btn_prod.sizePolicy().hasHeightForWidth())
        self.btn_prod.setSizePolicy(sizePolicy4)
        self.btn_prod.setFont(font)
        self.btn_prod.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.layout.addWidget(self.btn_prod, 1, 3, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy4.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy4)
        self.btn_5.setFont(font)
        self.btn_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_5.setIconSize(QSize(16, 16))

        self.layout.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_div = QPushButton(self.centralwidget)
        self.btn_div.setObjectName(u"btn_div")
        sizePolicy4.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy4)
        self.btn_div.setFont(font)
        self.btn_div.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_div.setIconSize(QSize(16, 16))

        self.layout.addWidget(self.btn_div, 0, 3, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy4.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy4)
        self.btn_9.setFont(font)
        self.btn_9.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_9.setIconSize(QSize(16, 16))

        self.layout.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy4.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy4)
        self.btn_4.setFont(font)
        self.btn_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_4.setIconSize(QSize(16, 16))

        self.layout.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_add = QPushButton(self.centralwidget)
        self.btn_add.setObjectName(u"btn_add")
        sizePolicy4.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy4)
        self.btn_add.setFont(font)
        self.btn_add.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_add.setIconSize(QSize(16, 16))

        self.layout.addWidget(self.btn_add, 3, 3, 1, 1)

        self.btn_sub = QPushButton(self.centralwidget)
        self.btn_sub.setObjectName(u"btn_sub")
        sizePolicy4.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
        self.btn_sub.setSizePolicy(sizePolicy4)
        self.btn_sub.setFont(font)
        self.btn_sub.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_sub.setIconSize(QSize(16, 16))

        self.layout.addWidget(self.btn_sub, 2, 3, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy4.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy4)
        self.btn_6.setFont(font)
        self.btn_6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_6.setIconSize(QSize(16, 16))

        self.layout.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy4.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy4)
        self.btn_2.setFont(font)
        self.btn_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_2.setIconSize(QSize(16, 16))

        self.layout.addWidget(self.btn_2, 3, 1, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy4.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy4)
        self.btn_1.setFont(font)
        self.btn_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_1.setIconSize(QSize(16, 16))

        self.layout.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_ce = QPushButton(self.centralwidget)
        self.btn_ce.setObjectName(u"btn_ce")
        sizePolicy4.setHeightForWidth(self.btn_ce.sizePolicy().hasHeightForWidth())
        self.btn_ce.setSizePolicy(sizePolicy4)
        self.btn_ce.setFont(font)
        self.btn_ce.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_ce.setIconSize(QSize(16, 16))

        self.layout.addWidget(self.btn_ce, 4, 0, 1, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy4.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy4)
        self.btn_0.setFont(font)
        self.btn_0.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_0.setIconSize(QSize(16, 16))

        self.layout.addWidget(self.btn_0, 4, 1, 1, 1)


        self.verticalLayout.addLayout(self.layout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator by Garanich", None))
        self.lbl_temp.setText("")
        self.le_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_point.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btn_clear_entry.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.btn_backspace.setText("")
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_eq.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.btn_prod.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_div.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_sub.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_ce.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi

