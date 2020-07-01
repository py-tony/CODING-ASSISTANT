# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(311, 431)
        Dialog.setMaximumSize(QtCore.QSize(311, 431))
        Dialog.setWindowOpacity(0.9)
        Dialog.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 320, 311, 23))
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.ca_brand = QtWidgets.QLabel(Dialog)
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
        self.login_label = QtWidgets.QLabel(Dialog)
        self.login_label.setGeometry(QtCore.QRect(120, 70, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.login_label.setFont(font)
        self.login_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.login_label.setObjectName("login_label")
        self.name_field = QtWidgets.QLineEdit(Dialog)
        self.name_field.setGeometry(QtCore.QRect(10, 140, 291, 31))
        self.name_field.setAutoFillBackground(False)
        self.name_field.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(130, 130, 130);")
        self.name_field.setInputMethodHints(QtCore.Qt.ImhNone)
        self.name_field.setText("")
        self.name_field.setMaxLength(20)
        self.name_field.setObjectName("name_field")
        self.password_field = QtWidgets.QLineEdit(Dialog)
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
        self.register_btn = QtWidgets.QPushButton(Dialog)
        self.register_btn.setGeometry(QtCore.QRect(110, 250, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.register_btn.setFont(font)
        self.register_btn.setMouseTracking(True)
        self.register_btn.setStyleSheet("background-color: rgb(121, 255, 97);")
        self.register_btn.setCheckable(True)
        self.register_btn.setObjectName("register_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_2.setText(_translate("Dialog", "Don\'t have an account yet?  Register now"))
        self.ca_brand.setText(_translate("Dialog", "CODE ASSISTANT"))
        self.login_label.setText(_translate("Dialog", "Log In"))
        self.name_field.setPlaceholderText(_translate("Dialog", "Username*"))
        self.password_field.setPlaceholderText(_translate("Dialog", "Password*"))
        self.register_btn.setText(_translate("Dialog", "Log In"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
