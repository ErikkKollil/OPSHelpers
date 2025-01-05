# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_OPSH_2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtCore import QSize, Qt
from instruction_windows import Ui_Tools_Windows
from hotkey_windows import Ui_Hot_Windows
from author_windows import Ui_About
import sys, os


def rpatha(filename):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        ICONS_DIR = os.path.join(BASE_DIR, '..', 'icons')
        return os.path.join(ICONS_DIR, filename)

class CustomLineEdit(object):
    def __init__(self, parent=None):
        super().__init__(parent)

    def contextMenuEvent(self, event):
        # Создаем кастомное меню
        menu = QMenu(self)

        # Добавляем действия на русском языке
        undo_action = QAction("Отменить", self)
        undo_action.triggered.connect(self.undo)
        menu.addAction(undo_action)

        redo_action = QAction("Повторить", self)
        redo_action.triggered.connect(self.redo)
        menu.addAction(redo_action)

        menu.addSeparator()

        cut_action = QAction("Вырезать", self)
        cut_action.triggered.connect(self.cut)
        menu.addAction(cut_action)

        copy_action = QAction("Копировать", self)
        copy_action.triggered.connect(self.copy)
        menu.addAction(copy_action)

        paste_action = QAction("Вставить", self)
        paste_action.triggered.connect(self.paste)
        menu.addAction(paste_action)

        menu.addSeparator()

        select_all_action = QAction("Выделить все", self)
        select_all_action.triggered.connect(self.selectAll)
        menu.addAction(select_all_action)

        # Отображаем меню
        menu.exec_(event.globalPos())

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 785)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 785))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 785))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(rpatha("rman.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setWindowFilePath("")
        MainWindow.setIconSize(QtCore.QSize(48, 48))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setToolTip("")
        self.centralwidget.setStatusTip("")
        self.centralwidget.setWhatsThis("")
        self.centralwidget.setAccessibleName("")
        self.centralwidget.setAccessibleDescription("")
        self.centralwidget.setStyleSheet("QWidget {\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.119318 rgba(196, 206, 255, 255), stop:1 rgba(146, 219, 255, 255));\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget_BD = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_BD.setGeometry(QtCore.QRect(20, 120, 1160, 541))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_BD.setFont(font)
        self.tableWidget_BD.setMouseTracking(False)
        self.tableWidget_BD.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget_BD.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget_BD.setStyleSheet("background-color: #e5f0ff;\n"
"border: 2px solid #4169e1;\n"
"border-radius: 1px;\n"
"border-width: 2px;\n"
"selection-background-color: rgb(0, 170, 255)\n"
"")
        self.tableWidget_BD.setFrameShape(QtWidgets.QFrame.Panel)
        self.tableWidget_BD.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget_BD.setLineWidth(1)
        self.tableWidget_BD.setMidLineWidth(3)
        self.tableWidget_BD.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget_BD.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_BD.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_BD.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_BD.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_BD.setObjectName("tableWidget_BD")
        self.tableWidget_BD.setColumnCount(3)
        self.tableWidget_BD.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_BD.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_BD.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        item.setFont(font)
        self.tableWidget_BD.setHorizontalHeaderItem(2, item)
        self.tableWidget_BD.verticalHeader().setVisible(False)
        self.lineEdit_search = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_search.setGeometry(QtCore.QRect(20, 70, 761, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_search.setFont(font)
        self.lineEdit_search.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_search.setStyleSheet("QLineEdit {\n"
                                                        "    background-color: #e5f0ff;\n"
                                                        "    border: 2px solid #4169e1;\n"
                                                        "    border-radius: 10px;\n"
                                                        "    border-width: 2px;    \n"
                                                        "    selection-background-color: rgb(0, 170, 255)\n"
                                                        "}\n"
                                                        "\n"
                                                        "QLineEdit:hover{\n"
                                                        "    background-color: #bdd7ff\n"
                                                        "}")
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.pushButton_home = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_home.setGeometry(QtCore.QRect(540, 670, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setStyleSheet("QPushButton{\n"
                                                        "    background-color: #e5f0ff;\n"
                                                        "    border: 2px solid #4169e1;\n"
                                                        "    border-radius: 10px;\n"
                                                        "    border-width: 2px;\n"
                                                        "    selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, \n"
                                                        "    stop: 0 #FF92BB, stop: 1 white);\n"
                                                        "}\n"
                                                        "\n"
                                                        "QPushButton:hover{\n"
                                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(172, 167, 255, 255), stop:1 rgba(135, 215, 255, 255))\n"
                                                        "}\n"
                                                        "\n"
                                                        "QPushButton:pressed{\n"
                                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(196, 192, 255, 255), stop:1 rgba(162, 224, 255, 255))\n"
                                                        "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(rpatha("h3.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_home.setIcon(icon1)
        self.pushButton_home.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_home.setObjectName("pushButton_home")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(240, 20, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setStyleSheet("QLineEdit {\n"
                                                        "    background-color: #e5f0ff;\n"
                                                        "    border: 2px solid #4169e1;\n"
                                                        "    border-radius: 10px;\n"
                                                        "    border-width: 2px;    \n"
                                                        "    selection-background-color: rgb(0, 170, 255)\n"
                                                        "}\n"
                                                        "\n"
                                                        "QLineEdit:hover{\n"
                                                        "    background-color: #bdd7ff\n"
                                                        "}")
        self.lineEdit_name.setInputMask("")
        self.lineEdit_name.setText("")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_date = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_date.setAlignment(Qt.AlignCenter)
        self.lineEdit_date.setGeometry(QtCore.QRect(660, 20, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_date.setFont(font)
        self.lineEdit_date.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_date.setStyleSheet("QLineEdit {\n"
                                                        "    background-color: #e5f0ff;\n"
                                                        "    border: 2px solid #4169e1;\n"
                                                        "    border-radius: 10px;\n"
                                                        "    border-width: 2px;    \n"
                                                        "    selection-background-color: rgb(0, 170, 255)\n"
                                                        "}\n"
                                                        "\n"
                                                        "QLineEdit:hover{\n"
                                                        "    background-color: #bdd7ff\n"
                                                        "}")
        self.lineEdit_date.setObjectName("lineEdit_date")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(1050, 20, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setToolTip("")
        self.pushButton_add.setStyleSheet("QPushButton{\n"
                                                        "    background-color: #e5f0ff;\n"
                                                        "    border: 2px solid #4169e1;\n"
                                                        "    border-radius: 10px;\n"
                                                        "    border-width: 2px;\n"
                                                        "    selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, \n"
                                                        "    stop: 0 #FF92BB, stop: 1 white);\n"
                                                        "}\n"
                                                        "\n"
                                                        "QPushButton:hover{\n"
                                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(172, 167, 255, 255), stop:1 rgba(135, 215, 255, 255))\n"
                                                        "}\n"
                                                        "\n"
                                                        "QPushButton:pressed{\n"
                                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(196, 192, 255, 255), stop:1 rgba(162, 224, 255, 255))\n"
                                                        "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(rpatha("add2.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_add.setIcon(icon2)
        self.pushButton_add.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_add.setObjectName("pushButton_add")
        self.label_info_add = QtWidgets.QLabel(self.centralwidget)
        self.label_info_add.setGeometry(QtCore.QRect(100, 20, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_info_add.setFont(font)
        self.label_info_add.setStyleSheet("background-color: none")
        self.label_info_add.setObjectName("label_info_add")
        self.pushButton_SortDate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SortDate.setGeometry(QtCore.QRect(330, 670, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_SortDate.setFont(font)
        self.pushButton_SortDate.setStyleSheet("QPushButton{\n"
                                                                "    background-color: #e5f0ff;\n"
                                                                "    border: 2px solid #4169e1;\n"
                                                                "    border-radius: 10px;\n"
                                                                "    border-width: 2px;\n"
                                                                "    selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, \n"
                                                                "    stop: 0 #FF92BB, stop: 1 white);\n"
                                                                "}\n"
                                                                "\n"
                                                                "QPushButton:hover{\n"
                                                                "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(172, 167, 255, 255), stop:1 rgba(135, 215, 255, 255))\n"
                                                                "}\n"
                                                                "\n"
                                                                "QPushButton:pressed{\n"
                                                                "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(196, 192, 255, 255), stop:1 rgba(162, 224, 255, 255))\n"
                                                                "}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(rpatha("sort.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_SortDate.setIcon(icon3)
        self.pushButton_SortDate.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_SortDate.setObjectName("pushButton_SortDate")
        self.pushButton_SortName = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SortName.setGeometry(QtCore.QRect(120, 670, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_SortName.setFont(font)
        self.pushButton_SortName.setStyleSheet("QPushButton{\n"
                                                                "    background-color: #e5f0ff;\n"
                                                                "    border: 2px solid #4169e1;\n"
                                                                "    border-radius: 10px;\n"
                                                                "    border-width: 2px;\n"
                                                                "    selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, \n"
                                                                "    stop: 0 #FF92BB, stop: 1 white);\n"
                                                                "}\n"
                                                                "\n"
                                                                "QPushButton:hover{\n"
                                                                "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(172, 167, 255, 255), stop:1 rgba(135, 215, 255, 255))\n"
                                                                "}\n"
                                                                "\n"
                                                                "QPushButton:pressed{\n"
                                                                "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(196, 192, 255, 255), stop:1 rgba(162, 224, 255, 255))\n"
                                                                "}")
        self.pushButton_SortName.setIcon(icon3)
        self.pushButton_SortName.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_SortName.setObjectName("pushButton_SortName")
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(870, 670, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setStyleSheet("QPushButton{\n"
                                                        "    background-color: #e5f0ff;\n"
                                                        "    border: 2px solid #4169e1;\n"
                                                        "    border-radius: 10px;\n"
                                                        "    border-width: 2px;\n"
                                                        "    selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, \n"
                                                        "    stop: 0 #FF92BB, stop: 1 white);\n"
                                                        "}\n"
                                                        "\n"
                                                        "QPushButton:hover{\n"
                                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(172, 167, 255, 255), stop:1 rgba(135, 215, 255, 255))\n"
                                                        "}\n"
                                                        "\n"
                                                        "QPushButton:pressed{\n"
                                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(196, 192, 255, 255), stop:1 rgba(162, 224, 255, 255))\n"
                                                        "}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(rpatha("trash.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_delete.setIcon(icon4)
        self.pushButton_delete.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.label_info_add_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_info_add_2.setGeometry(QtCore.QRect(970, 720, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_info_add_2.setFont(font)
        self.label_info_add_2.setStyleSheet("background-color: none")
        self.label_info_add_2.setObjectName("label_info_add_2")
        self.lineEdit_dop = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_dop.setGeometry(QtCore.QRect(790, 20, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_dop.setFont(font)
        self.lineEdit_dop.setStyleSheet("QLineEdit {\n"
"    background-color: #e5f0ff;\n"
"    border: 2px solid #4169e1;\n"
"    border-radius: 10px;\n"
"    border-width: 2px;    \n"
"    selection-background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    background-color: #bdd7ff\n"
"}")
        self.lineEdit_dop.setInputMask("")
        self.lineEdit_dop.setText("")
        self.lineEdit_dop.setObjectName("lineEdit_dop")
        self.pushButton_search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search.setGeometry(QtCore.QRect(1050, 70, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setStyleSheet("QPushButton{\n"
"    background-color: #e5f0ff;\n"
"    border: 2px solid #4169e1;\n"
"    border-radius: 10px;\n"
"    border-width: 2px;\n"
"    selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, \n"
"    stop: 0 #FF92BB, stop: 1 white);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(172, 167, 255, 255), stop:1 rgba(135, 215, 255, 255))\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(196, 192, 255, 255), stop:1 rgba(162, 224, 255, 255))\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(rpatha("search6.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_search.setIcon(icon5)
        self.pushButton_search.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_search.setObjectName("pushButton_search")
        self.pushButton_history = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_history.setGeometry(QtCore.QRect(710, 670, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_history.setFont(font)
        self.pushButton_history.setStyleSheet("QPushButton{\n"
"    background-color: #e5f0ff;\n"
"    border: 2px solid #4169e1;\n"
"    border-radius: 10px;\n"
"    border-width: 2px;\n"
"    selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, \n"
"    stop: 0 #FF92BB, stop: 1 white);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(172, 167, 255, 255), stop:1 rgba(135, 215, 255, 255))\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(196, 192, 255, 255), stop:1 rgba(162, 224, 255, 255))\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(rpatha("hist2.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off) # info_stories.ico
        self.pushButton_history.setIcon(icon6)
        self.pushButton_history.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_history.setObjectName("pushButton_history")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(1030, 670, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setStyleSheet("QPushButton{\n"
"    background-color: #e5f0ff;\n"
"    border: 2px solid #4169e1;\n"
"    border-radius: 10px;\n"
"    border-width: 2px;\n"
"    selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, \n"
"    stop: 0 #FF92BB, stop: 1 white);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(172, 167, 255, 255), stop:1 rgba(135, 215, 255, 255))\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(196, 192, 255, 255), stop:1 rgba(162, 224, 255, 255))\n"
"}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(rpatha("e2.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_exit.setIcon(icon7)
        self.pushButton_exit.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.pushButton_mark = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mark.setGeometry(QtCore.QRect(20, 670, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_mark.setFont(font)
        self.pushButton_mark.setStyleSheet("QPushButton{\n"
"    background-color: #e5f0ff;\n"
"    border: 2px solid #4169e1;\n"
"    border-radius: 10px;\n"
"    border-width: 2px;\n"
"    selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, \n"
"    stop: 0 #FF92BB, stop: 1 white);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(172, 167, 255, 255), stop:1 rgba(135, 215, 255, 255))\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(196, 192, 255, 255), stop:1 rgba(162, 224, 255, 255))\n"
"}")
        self.pushButton_mark.setText("")
        icon8 = QtGui.QIcon() 
        icon8.addPixmap(QtGui.QPixmap(rpatha("wh4.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off) # wh.png
        self.pushButton_mark.setIcon(icon8)
        self.pushButton_mark.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_mark.setObjectName("pushButton_mark")
        self.pushButton_print = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_print.setGeometry(QtCore.QRect(20, 20, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_print.setFont(font)
        self.pushButton_print.setStyleSheet("QPushButton{\n"
"    background-color: #e5f0ff;\n"
"    border: 2px solid #4169e1;\n"
"    border-radius: 10px;\n"
"    border-width: 2px;\n"
"    selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, \n"
"    stop: 0 #FF92BB, stop: 1 white);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(172, 167, 255, 255), stop:1 rgba(135, 215, 255, 255))\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(196, 192, 255, 255), stop:1 rgba(162, 224, 255, 255))\n"
"}")
        self.pushButton_print.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(rpatha("printer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_print.setIcon(icon9)
        self.pushButton_print.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_print.setObjectName("pushButton_print")
        self.lineEdit_date_4 = QtWidgets.QLineEdit(self.centralwidget)
        #self.lineEdit_date_4.setAlignment(Qt.AlignCenter)
        self.lineEdit_date_4.setGeometry(QtCore.QRect(790, 70, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lineEdit_date_4.setFont(font)
        self.lineEdit_date_4.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_date_4.setStyleSheet("QLineEdit {\n"
"    background-color: #e5f0ff;\n"
"    border: 2px solid #4169e1;\n"
"    border-radius: 10px;\n"
"    border-width: 2px;    \n"
"    selection-background-color: rgb(0, 170, 255)\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    background-color: #bdd7ff\n"
"}")
        self.lineEdit_date_4.setObjectName("lineEdit_date_4")
        self.lineEdit_date_4.setAlignment(Qt.AlignCenter)
        self.lineEdit_date_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_date_5.setGeometry(QtCore.QRect(920, 70, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lineEdit_date_5.setFont(font)
        self.lineEdit_date_5.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_date_5.setStyleSheet("QLineEdit {\n"
"    background-color: #e5f0ff;\n"
"    border: 2px solid #4169e1;\n"
"    border-radius: 10px;\n"
"    border-width: 2px;    \n"
"    selection-background-color: rgb(0, 170, 255)\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    background-color: #bdd7ff\n"
"}")
        self.lineEdit_date_5.setObjectName("lineEdit_date_5")
        self.lineEdit_date_5.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setToolTip("")
        self.menubar.setAccessibleName("")
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.menu.setFont(font)
        self.menu.setObjectName("menu")
        #self.menu_2 = QtWidgets.QMenu(self.menubar)
        MainWindow.setMenuBar(self.menubar)

        self.action_tool = QtWidgets.QAction(MainWindow)
        self.action_tool.setObjectName("action_tool")

        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")

        self.action_hotbutton = QtWidgets.QAction(MainWindow)
        self.action_hotbutton.setObjectName("action_hotbutton")

        #self.menubar.addAction(self.menu.menuAction()) #Создать подменю в меню

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OPSHelper v 2.1"))
        self.tableWidget_BD.setSortingEnabled(False)

        # Добавляем шрифт для клавши
        font_id = QFontDatabase.addApplicationFont("style/Roboto-Black.ttf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        custom_font_1 = QFont(font_family, 11) 

        # Добавляем шрифт для подсказок
        font_ids = QFontDatabase.addApplicationFont("style/Roboto-Light.ttf")
        font_familys = QFontDatabase.applicationFontFamilies(font_ids)[0]
        custom_fonts_1 = QFont(font_familys, 10)  
        custom_fonts_2 = QFont(font_familys, 9)

        # Столбцы таблицы
        item = self.tableWidget_BD.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Наименование"))
        item.setFont(custom_fonts_2)
        item = self.tableWidget_BD.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Срок годности"))
        item.setFont(custom_fonts_2)
        item = self.tableWidget_BD.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Дополнительная информация"))
        item.setFont(custom_fonts_2)
        item.setSizeHint(QSize(1, 27)) # --------------------------- Задать высоту заголовка

        # Информация
        self.label_info_add.setText(_translate("MainWindow", "Новый элемент:"))
        self.label_info_add.setFont(custom_fonts_1)
        self.label_info_add_2.setToolTip(_translate("MainWindow", "Разработал Козин Егор Технополис \"ЭРА\" для своей мамы"))
        self.label_info_add_2.setText(_translate("MainWindow", "© 2022 ЭРА. Все права защищены."))

        # Подсказки
        self.lineEdit_search.setPlaceholderText(_translate("MainWindow", " Поиск по имени "))
        self.lineEdit_search.setFont(custom_fonts_2)
        self.lineEdit_name.setPlaceholderText(_translate("MainWindow", " Наименование"))
        self.lineEdit_name.setFont(custom_fonts_2)
        self.lineEdit_date.setPlaceholderText(_translate("MainWindow", " Срок годности"))
        self.lineEdit_date.setFont(custom_fonts_2)
        self.lineEdit_dop.setPlaceholderText(_translate("MainWindow", " Дополнительная информация"))
        self.lineEdit_dop.setFont(custom_fonts_2)
        self.lineEdit_date_4.setPlaceholderText(_translate("MainWindow", " Начало периода"))
        self.lineEdit_date_4.setFont(custom_fonts_2)
        self.lineEdit_date_5.setPlaceholderText(_translate("MainWindow", " Конец периода"))
        self.lineEdit_date_5.setFont(custom_fonts_2)

        # Клавиши
        self.pushButton_home.setToolTip(_translate("MainWindow", "Перейти к общему списку"))
        self.pushButton_home.setText(_translate("MainWindow", " Домой"))
        self.pushButton_home.setFont(custom_font_1)
        self.pushButton_add.setText(_translate("MainWindow", " Добавить"))
        self.pushButton_add.setFont(custom_font_1)
        self.pushButton_SortDate.setText(_translate("MainWindow", " Срок годности"))
        self.pushButton_SortDate.setFont(custom_font_1)
        self.pushButton_SortName.setText(_translate("MainWindow", " Наименование"))
        self.pushButton_SortName.setFont(custom_font_1)
        self.pushButton_delete.setText(_translate("MainWindow", " Удалить"))
        self.pushButton_delete.setFont(custom_font_1)
        self.pushButton_search.setText(_translate("MainWindow", " Поиск"))
        self.pushButton_search.setFont(custom_font_1)
        self.pushButton_history.setText(_translate("MainWindow", " История"))
        self.pushButton_history.setFont(custom_font_1)
        self.pushButton_exit.setText(_translate("MainWindow", " Выход"))
        self.pushButton_exit.setFont(custom_font_1)

        self.pushButton_mark.setToolTip(_translate("MainWindow", "Работа со складом"))
        self.pushButton_history.setToolTip(_translate("MainWindow", "Здесь хранится вся история за последние 180 дней"))

        #self.menu.setTitle(_translate("MainWindow", "Инструкция")) # Кнопка меню 1
        
        #self.menu.addAction(self.action_hotbutton) # Подкнопка 1
        #self.action_hotbutton.setText(_translate("MainWindow", "& Горячие клавиши"))
        #self.action_hotbutton.triggered.connect(lambda: self.call_hot())

        #self.menu.addAction(self.action_tool) # Подкнопка 2
        #self.action_tool.setText(_translate("MainWindow", "& Открыть инструкцию"))
        #self.action_tool.triggered.connect(lambda: self.call_tools()) #lambda: print('TOOLS'))

        self.menubar.addAction(self.action_tool) # Задать действие в меню
        self.action_tool.setText(_translate("MainWindow", "& Инструкция")) # Назвать кнопку в меню
        self.action_tool.triggered.connect(lambda: self.call_tools())  # Задать действие при нажатии на клавишу
        self.action_tool.setFont(custom_fonts_1)

        self.menubar.addAction(self.action_hotbutton)
        self.action_hotbutton.setText(_translate("MainWindow", "& Горячие клавиши"))
        self.action_hotbutton.triggered.connect(lambda: self.call_hot()) 
        self.action_hotbutton.setFont(custom_fonts_1)

        self.menubar.addAction(self.action_about)
        self.action_about.setText(_translate("MainWindow", "& О программе"))
        self.action_about.triggered.connect(lambda: self.call_about()) 
        self.action_about.setFont(custom_fonts_1)
    
    # Функция вывода окна истории
    def call_tools(self):
        self.tool = WinTools() # Окно истории
        self.tool.show() # Вывод окна

    # Функция вывода окна истории
    def call_hot(self):
        self.hot = WinHot() # Окно истории
        self.hot.show() # Вывод окна
    
    # Функция вывода окна истории
    def call_about(self):
        self.hot = WinAbout() # Окно истории
        self.hot.show() # Вывод окна

class WinTools(QtWidgets.QWidget, Ui_Tools_Windows): 

    def __init__(self, parent=None):
        super(WinTools, self).__init__(parent)
        self.setupUi(self)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~TOOLS~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


class WinHot(QtWidgets.QWidget, Ui_Hot_Windows): 

    def __init__(self, parent=None):
        super(WinHot, self).__init__(parent)
        self.setupUi(self)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~HOT~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


class WinAbout(QtWidgets.QWidget, Ui_About): 

    def __init__(self, parent=None):
        super(WinAbout, self).__init__(parent)
        self.setupUi(self)
        self.click_button()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~ABOUT~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    def click_button(self):
        self.pushButton.clicked.connect(self.butt_exit_about)

    def butt_exit_about(self):
        self.close() # Закрывает окно программы

    def keyPressEvent(self, event): # О клавишах (https://doc.qt.io/qt-5/qt.html)
        if event.key() == Qt.Key_Escape : 
            print('Вы нажали на Escape')
            self.butt_exit_about() 
        else:
            pass # Заглушка


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow = CustomLineEdit()
    MainWindow.setPlaceholderText("ПКМ для контекстного меню")
    MainWindow.show()
    sys.exit(app.exec_())