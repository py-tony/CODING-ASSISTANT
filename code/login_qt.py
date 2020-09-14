# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login_win(object):
    def setupUi(self, Login_win):
        Login_win.setObjectName("Login_win")
        Login_win.resize(311, 431)
        Login_win.setMaximumSize(QtCore.QSize(311, 431))
        Login_win.setWindowOpacity(0.9)
        Login_win.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.register_link = QtWidgets.QPushButton(Login_win)
        self.register_link.setGeometry(QtCore.QRect(0, 320, 311, 23))
        self.register_link.setStyleSheet("color: rgb(255, 255, 255);")
        self.register_link.setObjectName("register_link")
        self.ca_brand = QtWidgets.QLabel(Login_win)
        self.ca_brand.setEnabled(True)
        self.ca_brand.setGeometry(QtCore.QRect(70, 30, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ca_brand.setFont(font)
        self.ca_brand.setAutoFillBackground(False)
        self.ca_brand.setStyleSheet("color: rgb(255, 255, 255);")
        self.ca_brand.setObjectName("ca_brand")
        self.login_label = QtWidgets.QLabel(Login_win)
        self.login_label.setGeometry(QtCore.QRect(120, 70, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.login_label.setFont(font)
        self.login_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.login_label.setObjectName("login_label")
        self.name_field = QtWidgets.QLineEdit(Login_win)
        self.name_field.setGeometry(QtCore.QRect(10, 140, 291, 31))
        self.name_field.setAutoFillBackground(False)
        self.name_field.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(130, 130, 130);")
        self.name_field.setInputMethodHints(QtCore.Qt.ImhNone)
        self.name_field.setText("")
        self.name_field.setMaxLength(20)
        self.name_field.setObjectName("name_field")
        self.password_field = QtWidgets.QLineEdit(Login_win)
        self.password_field.setGeometry(QtCore.QRect(10, 190, 291, 31))
        self.password_field.setAutoFillBackground(False)
        self.password_field.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(130, 130, 130);")
        self.password_field.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.password_field.setText("")
        self.password_field.setMaxLength(50)
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_field.setClearButtonEnabled(False)
        self.password_field.setObjectName("password_field")
        self.register_btn = QtWidgets.QPushButton(Login_win)
        self.register_btn.setGeometry(QtCore.QRect(110, 250, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.register_btn.setFont(font)
        self.register_btn.setMouseTracking(True)
        self.register_btn.setStyleSheet("background-color: rgb(121, 255, 97);")
        self.register_btn.setCheckable(True)
        self.register_btn.setObjectName("register_btn")

        self.retranslateUi(Login_win)
        QtCore.QMetaObject.connectSlotsByName(Login_win)

    def retranslateUi(self, Login_win):
        _translate = QtCore.QCoreApplication.translate
        Login_win.setWindowTitle(_translate("Login_win", "Dialog"))
        self.register_link.setText(_translate("Login_win", "Don\'t have an account yet?  Register now"))
        self.ca_brand.setText(_translate("Login_win", "CODE ASSISTANT"))
        self.login_label.setText(_translate("Login_win", "Log In"))
        self.name_field.setPlaceholderText(_translate("Login_win", "Username*"))
        self.password_field.setPlaceholderText(_translate("Login_win", "Password*"))
        self.register_btn.setText(_translate("Login_win", "Log In"))
