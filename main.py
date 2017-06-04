# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#QHBoxLayout
# WARNING! All changes made in this file will be lost!
import sys,parser
from PyQt5 import QtCore
from PyQt5.QtWidgets import QInputDialog,QCheckBox,QVBoxLayout,QGroupBox
from PyQt5.QtWidgets import QHBoxLayout,QApplication, QWidget, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QLabel, QTextEdit, QPushButton, QMainWindow
from PyQt5.QtWidgets import QAction, QFileDialog
from PyQt5.QtGui import QIcon

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class OpenFile(QMainWindow):
   def __init__(self, parent=None):
       QMainWindow.__init__(self, parent)
       self.setGeometry(300, 300, 350, 300)
       self.setWindowTitle('OpenFile')
       self.textEdit = QTextEdit()
       self.setCentralWidget(self.textEdit)
       self.statusBar()
       self.setFocus()
       exit = QAction(QIcon('open.png'), 'Open', self)
       exit.setShortcut('Ctrl+O')
       exit.setStatusTip('Open new File')
    #    self.connect(exit, QtCore.SIGNAL('triggered()'), self.showDialog)

       menubar = self.menuBar()
       file = menubar.addMenu('&File')
       file.addAction(exit)

   def showDialog(self):
       (filename, ok) = QFileDialog.getOpenFileName(self, 'Open file', './')
       return filename

   def showSaveDialog(self):
       (filename, ok) = QFileDialog.getSaveFileName(self, 'Save file', './')
       return filename

class Ui_Form(object):
    fileUser = ''
    def start(self,event):
        parser.splitCode(self.lineEditVK.text(),self.lineEditT.text(),self.code.toPlainText(),str(self.checkBoxT.checkState()),str(self.checkBoxVK.checkState()))

    def openFile(self, event):
        fileUser = OpenFile().showDialog()
        f = open(fileUser,'r')
        self.code.setText(f.read())
        f.close()

    def saveFile(self,event):
        fileUser = OpenFile().showSaveDialog()
        f = open(fileUser,'w')
        f.write(self.code.toPlainText())
        f.close()

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("BotMather"))
        Form.setEnabled(True)
        Form.resize(800, 600)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        Form.setMaximumSize(QtCore.QSize(800, 600))
        Form.setAutoFillBackground(False)
        self.help = QLabel(Form)
        self.help.setGeometry(QtCore.QRect(480, 90, 281, 451))
        self.help.setStyleSheet(_fromUtf8(""))
        self.help.setTextFormat(QtCore.Qt.AutoText)
        self.help.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.help.setWordWrap(True)
        self.help.setObjectName(_fromUtf8("help"))
        self.widget = QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 0, 761, 81))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEditVK = QLineEdit(self.widget)
        self.lineEditVK.setMaximumSize(QtCore.QSize(180, 26))
        self.lineEditVK.setStyleSheet(_fromUtf8("border:0;"))
        self.lineEditVK.setObjectName(_fromUtf8("lineEditVK"))
        self.horizontalLayout_2.addWidget(self.lineEditVK)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEditT = QLineEdit(self.widget)
        self.lineEditT.setMaximumSize(QtCore.QSize(180, 26))
        self.lineEditT.setStyleSheet(_fromUtf8("border:0;"))
        self.lineEditT.setObjectName(_fromUtf8("lineEditT"))
        self.horizontalLayout.addWidget(self.lineEditT)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.widget1 = QWidget(self.groupBox)
        self.widget1.setGeometry(QtCore.QRect(10, 20, 108, 48))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.checkBoxT = QCheckBox(self.widget1)
        self.checkBoxT.setObjectName(_fromUtf8("checkBoxT"))
        self.verticalLayout.addWidget(self.checkBoxT)
        self.checkBoxVK = QCheckBox(self.widget1)
        self.checkBoxVK.setObjectName(_fromUtf8("checkBoxVK"))
        self.verticalLayout.addWidget(self.checkBoxVK)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.widget2 = QWidget(Form)
        self.widget2.setGeometry(QtCore.QRect(10, 90, 461, 491))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.verticalLayout_2 = QVBoxLayout(self.widget2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.code = QTextEdit(self.widget2)
        self.code.setStyleSheet(_fromUtf8("font: 11pt \"Free Avant Garde\";"))
        self.code.setObjectName(_fromUtf8("code"))
        self.verticalLayout_2.addWidget(self.code)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.save = QPushButton(self.widget2)
        self.save.setStyleSheet(_fromUtf8("QPushButton { \n"
"color: #fff; /* цвет текста */\n"
"  text-decoration: none; /* убирать подчёркивание у ссылок */\n"
"  background: rgb(212,75,56); /* фон кнопки */\n"
"  padding: .7em 1.5em; /* отступ от текста */\n"
"  outline: none; /* убирать контур в Mozilla */\n"
"border:0;}\n"
"QPushButton:hover { background: rgb(232,95,76); } /* при наведении курсора мышки */\n"
"QPushButton:active{background: rgb(152,15,0);  }/* при нажатии */"))
        self.save.setObjectName(_fromUtf8("save"))
        self.horizontalLayout_4.addWidget(self.save)
        self.load = QPushButton(self.widget2)
        self.load.setStyleSheet(_fromUtf8("QPushButton { \n"
"color: #fff; /* цвет текста */\n"
"  text-decoration: none; /* убирать подчёркивание у ссылок */\n"
"  background: rgb(212,75,56); /* фон кнопки */\n"
"  padding: .7em 1.5em; /* отступ от текста */\n"
"  outline: none; /* убирать контур в Mozilla */\n"
"border:0;}\n"
"QPushButton:hover { background: rgb(232,95,76); } /* при наведении курсора мышки */\n"
"QPushButton:active{background: rgb(152,15,0);  }/* при нажатии */"))
        self.load.setObjectName(_fromUtf8("load"))
        self.horizontalLayout_4.addWidget(self.load)
        self.pushButton = QPushButton(self.widget2)
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton { \n"
"color: #fff; /* цвет текста */\n"
"  text-decoration: none; /* убирать подчёркивание у ссылок */\n"
"  background: #FFC107; /* фон кнопки */\n"
"  padding: .7em 1.5em; /* отступ от текста */\n"
"  outline: none; /* убирать контур в Mozilla */\n"
"border:0;}\n"
"QPushButton:hover { background: #FFCA28; } /* при наведении курсора мышки */\n"
"QPushButton:active{background: #FFB300;  }/* при нажатии */"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.groupBox.raise_()
        self.pushButton.raise_()
        self.code.raise_()
        self.help.raise_()
        self.load.raise_()
        self.save.raise_()
        self.label_2.setBuddy(self.lineEditVK)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lineEditVK, self.lineEditT)
        Form.setTabOrder(self.lineEditT, self.pushButton)
        Form.setTabOrder(self.pushButton, self.checkBoxT)
        Form.setTabOrder(self.checkBoxT, self.checkBoxVK)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.help.setText(_translate("Form", "Справка:", None))
        self.label_2.setText(_translate("Form", "Ключ для TelegramBot:", None))
        self.label.setText(_translate("Form", "Ключ для VkBot:", None))
        self.groupBox.setTitle(_translate("Form", "Запуск после формирования:", None))
        self.checkBoxT.setText(_translate("Form", "TgBot", None))
        self.checkBoxVK.setText(_translate("Form", "VkBot", None))
        self.save.setText(_translate("Form", "Сохранить", None))
        self.load.setText(_translate("Form", "Загрузить", None))
        self.pushButton.setText(_translate("Form", "Сформировать ", None))

        self.pushButton.clicked.connect(self.start)
        self.load.clicked.connect(self.openFile)
        self.save.clicked.connect(self.saveFile)
        self.code.setText(u'''text(Print, yes):="Hello cat"?"Котики"
text(Print1):="Hello"?"Солнце"
geo(Geo?,sdf?):=$geo(Сбербанк)?"Геоданные"
text(банкомат):=$geo(Сбербанк)?"Банкоматы Сбербанка"
text(погода):=$weather(Novosibirsk)?"Погода в Новосибирске"
text(курс мне,курс):=$kurs(USD)?"курс USA"''')
        self.lineEditT.setText("398702729:AAGEbX17tBg8KBRbykgoeYbbOIX2bYWXMTc")
        self.lineEditVK.setText("198ea0ffd479982bf90ff58d16f0d12d08fa470b1835310fe14e035a23bb3d000aed0caa6761006fdd67c")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
