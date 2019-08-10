# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insertWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("background-color: rgb(53, 53, 53);")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(239, 239, 239);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 230, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Bodoni 72 Oldstyle")
        font.setPointSize(36)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 90, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(239, 239, 239);")
        self.label.setObjectName("label")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 140, 251, 31))
        self.lineEdit_3.setStyleSheet("color: rgb(181, 181, 181);\n"
"font: 14pt \".SF NS Text\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(239, 239, 239);")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 40, 251, 31))
        self.lineEdit.setStyleSheet("color: rgb(181, 181, 181);\n"
"font: 14pt \".SF NS Text\";")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(290, 200, 71, 31))
        self.pushButton.setStyleSheet("background-color: rgb(111, 111, 111);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 90, 251, 31))
        self.lineEdit_2.setStyleSheet("color: rgb(181, 181, 181);\n"
"font: 14pt \".SF NS Text\";")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Insert"))
        self.label_3.setText(_translate("Dialog", "Year"))
        self.label_4.setText(_translate("Dialog", "DoIHave 2"))
        self.label.setText(_translate("Dialog", "Title"))
        self.label_2.setText(_translate("Dialog", "Author"))
        self.pushButton.setText(_translate("Dialog", "OK"))
