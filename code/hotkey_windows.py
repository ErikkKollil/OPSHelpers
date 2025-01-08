# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HOT_OPS.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import sys, os

def rpatha(filename):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ICONS_DIR = os.path.join(BASE_DIR, '..', 'icons')
    return os.path.join(ICONS_DIR, filename)

class Ui_Hot_Windows(object):
    def setupUi(self, Hot_Windows):

        def rpath(relative_path):
            try:
                base_path = sys._MEIPASS
            except Exception:
                base_path = os.path.abspath(".")
            return os.path.join(base_path, relative_path)

        Hot_Windows.setObjectName("Hot_Windows")
        Hot_Windows.resize(677, 311)
        Hot_Windows.setMinimumSize(QtCore.QSize(677, 311))
        Hot_Windows.setMaximumSize(QtCore.QSize(677, 311))
        Hot_Windows.setWindowModality(QtCore.Qt.ApplicationModal)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(rpatha("ghelp.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Hot_Windows.setWindowIcon(icon)
        Hot_Windows.setStyleSheet("QWidget {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.142045 rgba(187, 183, 250, 255), stop:1 rgba(148, 212, 245, 255));\n"
"}")
        self.textEdit = QtWidgets.QTextEdit(Hot_Windows)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 655, 291))
        self.textEdit.setMinimumSize(QtCore.QSize(655, 291))
        self.textEdit.setMaximumSize(QtCore.QSize(655, 291))
        self.textEdit.setStyleSheet("background-color:none;")
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)

        self.retranslateUi(Hot_Windows)
        QtCore.QMetaObject.connectSlotsByName(Hot_Windows)

    def keyPressEvent(self, event): # О клавишах: https://doc.qt.io/qt-5/qt.html
        if event.key() == Qt.Key_Escape : # Клавиша ESC
            print('Вы нажали на Escape')
            self.close()

    def retranslateUi(self, Hot_Windows):
        _translate = QtCore.QCoreApplication.translate
        Hot_Windows.setWindowTitle(_translate("Hot_Windows", "OPSHelper v 2.4 - Горячие клавиши"))
        self.textEdit.setHtml(_translate("Hot_Windows", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Работа горячими клавишами:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• </span><span style=\" font-size:10pt; font-weight:600;\">Еnter</span><span style=\" font-size:10pt;\"> - Производит поиск данных, после заполнения поля поиска.<br />Аналогична нажатию кнопки &quot;Поиск&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• </span><span style=\" font-size:10pt; font-weight:600;\">Delete</span><span style=\" font-size:10pt;\"> - Производит удаление данных, после выделения строки.<br />Аналогична нажатию кнопки &quot;Удалить&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• </span><span style=\" font-size:10pt; font-weight:600;\">Esc</span><span style=\" font-size:10pt;\"> - Осуществляет выход из приложения или активного окна.<br />Аналогична нажатию кнопки &quot;Выход&quot; в случае с главным окном.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• </span><span style=\" font-size:10pt; font-weight:600;\">Home</span><span style=\" font-size:10pt;\"> - Осуществляет возвращение к общим (полным) данным.<br />Аналогична нажатию кнопки &quot;Домой&quot; .</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">• </span><span style=\" font-size:10pt; font-weight:600;\">F1</span><span style=\" font-size:10pt;\"> - Производит добавление или снятие товара со склада.<br />Аналогична нажатию кнопки &quot;✔&quot; (галочки).</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Hot_Windows = QtWidgets.QWidget()
    ui = Ui_Hot_Windows()
    ui.setupUi(Hot_Windows)
    Hot_Windows.show()
    sys.exit(app.exec_())

