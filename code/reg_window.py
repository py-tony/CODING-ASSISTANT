from urllib.request import urlopen
from validate_email import validate_email
import random
import time
import datetime
import yagmail
#local classes==============
from db import Database as db
from main_window_qt import Ui_CODE_ASSISTANT
from reg_qt import Ui_Frame
from login_qt import Ui_Login_win
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QRadioButton


class RegisterWindow(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        
        self.ui.register_btn.clicked.connect(self.register)

        self.ui.female_check.toggled.connect(self.onClicked)
        self.ui.male_check.toggled.connect(self.onClicked)
        self.gender = ""

    def onClicked(self):
        
        radioBtn = self.sender()
        if radioBtn.isChecked():
            
            self.gender = radioBtn.text()
        else:
            self.genger = ""

    def open_reg_win(self):
        
        
        self.Frame = QtWidgets.QFrame()
        self.ui = Ui_Frame()
        self.ui.setupUi(self.Frame)
        self.Frame.show()

        self.ui.register_btn.clicked.connect(self.register)
        # self.ui.female_check.toggled.connect(self.onClicked)
        # self.ui.male_check.toggled.connect(self.onClicked)
        

    def save_registration(self, username, email, phone,password, gender):
        
        data = db("code_assistant.db")
        
        result = data.insert(username, email, phone,password,gender)
        
        if result:
            QtWidgets.QMessageBox.critical(self,"Registration Fail", str(result))
            self.hide()
            self.open_reg_win()
        else:
            self.confirmation_email(email, username, password)
            
        
        valid = False
        print("all good")
        # self.Frame.hide()
        


    def register(self):


        #getting user input from the register form
        username = self.ui.name_field.text()
        email = self.ui.email_field.text()
        phone = self.ui.phone_field.text()
        password = self.ui.password_field.text()
        password_confirm = self.ui.password.text()
        self.ui.female_check.toggled.connect(self.onClicked)
        self.ui.male_check.toggled.connect(self.onClicked)
        print(self.gender)
        try:
            conn = validate_email(email) 
            print(conn)
        except Exception as e:
            email_error = e
            conn = False
        
        
        if len(username) < 2:
            QtWidgets.QMessageBox.critical(self, "Username Error",  "Invalid Username")
            self.hide()
            self.open_reg_win()

        elif conn == False:
            QtWidgets.QMessageBox.critical(self, "Email Error",  f"{conn} Invalid Email \nPlease make sure you provide a valid email where you can receive your confirmation message")
            self.hide()
            self.open_reg_win()

        elif len(password) < 6:
            QtWidgets.QMessageBox.critical(self, "Password Error",  "Invalid Password lenght! \nLenght password must be at least 6 characters")
            self.hide()
            self.open_reg_win()

        elif password != password_confirm:
                   
            QtWidgets.QMessageBox.critical(self, "Passoword Error",  "Passwords does not Match")
            self.hide()
            self.open_reg_win()
     

        else:
            self.save_registration(username, email, phone, password, self.gender)


        



    
    def confirmation_email(self, receiver, user_info, pass_info):

        sender = "codeassistantconfirm@gmail.com"      
        receiver = receiver
        password = "0990525794"
        

        msg = f"""
        Subject: CODE ASSISTANT CONFIRMATION EMAIL

        Username: {user_info}
        Password: {pass_info}
        
        
        Please click the link below to confirm your email
        https://py-tony.netlify.app/emailConfirm/




        If you do not recognize this please report at
        https://py-tony.netlify.app/repportSpam/


        """

        print("sending")
        try:
            
            
            yag = yagmail.SMTP(sender, password)
            yag.send(receiver, "CODE ASSISTANT REGISTRATION CONFIRMATION", msg)
            QtWidgets.QMessageBox.information(self, "Registration Succeeded",  "You've successfully registered on CA\nplease check your email to complete registration")
            self.Frame.hide()

            print("success")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Registration Failed", str(e))
            self.hide()
            self.open_reg_win()

            print(e)








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = RegisterWindow()
    window.open_reg_win()
    sys.exit(app.exec_())

