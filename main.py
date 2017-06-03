# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys,parser
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QLabel, QTextEdit, QPushButton

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)



class Ui_Form(object):

    def start(self,event):
        parser.splitCode(self.lineEditVK.text(),self.lineEditT.text(),self.code.toPlainText())

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(450, 413)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 431, 391))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEditVK = QLineEdit(self.gridLayoutWidget)
        self.lineEditVK.setObjectName(_fromUtf8("lineEditVK"))
        self.gridLayout.addWidget(self.lineEditVK, 0, 1, 1, 1)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.code = QTextEdit(self.gridLayoutWidget)
        self.code.setObjectName(_fromUtf8("code"))
        self.gridLayout.addWidget(self.code, 2, 1, 1, 1)
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditT = QLineEdit(self.gridLayoutWidget)
        self.lineEditT.setObjectName(_fromUtf8("lineEditT"))
        self.gridLayout.addWidget(self.lineEditT, 1, 1, 1, 1)
        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Ключ ВК", None))
        self.label_2.setText(_translate("Form", "Ключ Telegram", None))
        self.pushButton.setText(_translate("Form", "Сформировать", None))
        #Form.connect(pushButton,QtCore.SIGNAL('clicked()'),QtCore.SLOT('start()'))
        self.pushButton.clicked.connect(self.start)
        self.code.setText(u'''text(Print):="Hello cat"?"Котики"
text(Print1):="Hello"?"Солнце"
geo(Geo?):=$geo(Сбербанк)?"Геоданные"
text(курс мне):=$kurs(usa)?"курс USA''')
        self.lineEditT.setText("398702729:AAGEbX17tBg8KBRbykgoeYbbOIX2bYWXMTc")
        self.lineEditVK.setText("198ea0ffd479982bf90ff58d16f0d12d08fa470b1835310fe14e035a23bb3d000aed0caa6761006fdd67c")

if __name__ == "__main__":

    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    sys.exit(app.exec_())
