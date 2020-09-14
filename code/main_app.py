
from urllib.request import urlopen
from validate_email import validate_email
import random
import time
import datetime
import yagmail
#local classes==============
from db import Database as db
from main_window_qt import Ui_CODE_ASSISTANT as main
from reg_qt import Ui_Frame
from login_qt import Ui_Login_win
from reg_window import RegisterWindow
# pqt classes
import sys
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QSlider, QSizePolicy,QStyle, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon , QPalette
from PyQt5.QtCore import Qt, QUrl

class LoginWindow(QtWidgets.QWidget, main):
    global logged_in
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_Login_win()
        self.ui.setupUi(self)
        self.ui.register_btn.clicked.connect(self.authenticate)
        self.ui.register_link.clicked.connect(self.reg_win)
    
    

    def authenticate(self):
        username = self.ui.name_field.text()
        password = self.ui.password_field.text()

        
        

        data = db("code_assistant.db")
        records = data.fetch()
        print(records)
        for i in records:
            if username and password in i:
                

                data = db("code_assistant.db") # db is the database
                data.insert_hist(username)
                print(data.fetch_hist())
                
                QtWidgets.QMessageBox.information(self, "Success", "YOu're good to go")
                logged_in = True
                
                self.main_window()
                self.close()
                
                break
                
                
        else:
            QtWidgets.QMessageBox.critical(self, "Fail",  "Username or Password incorrect")


    def reg_win(self):

        
        self.window = RegisterWindow()
        self.window.open_reg_win()

    
    

    def media_player(self):
        # create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        # create videowidget object
        video_widget = QVideoWidget()

        open_btn = QPushButton("Open Video")
        open_btn.clicked.connect(self.open_file)

        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False) 
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)
  
        
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)
        self.slider.sliderMoved.connect(self.set_position)

        #create Label
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)


        #creat hbox layout
        self.ui_main.verticalLayout_15.addWidget(video_widget)

        
        horizontalLayout = QHBoxLayout()
        horizontalLayout.setContentsMargins(0,0,0,0)        

        # set widgets to  the hbox layout

        horizontalLayout.addWidget(open_btn)
        horizontalLayout.addWidget(self.playBtn)
        horizontalLayout.addWidget(self.slider)
        
        self.ui_main.verticalLayout_15.addLayout(horizontalLayout)


        self.mediaPlayer.setVideoOutput(video_widget)

        # media play signal
        self.mediaPlayer.stateChanged.connect(self.media_state_change)
        
        # duration changed
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Video")


        
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(file_name)))
        self.playBtn.setEnabled(True)

        

    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play() 

    def media_state_change(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))

        else:
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def position_changed(self, position):
        self.slider.setValue(position)

    def duration_changed(self, duration):
        self.slider.setRange(0, duration)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

    def main_window(self):
        
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui_main = main()
        
        self.ui_main.setupUi(self.MainWindow)
        self.media_player()
        self.MainWindow.show()









if __name__ == "__main__":

    logged_in = False
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = LoginWindow()

    # Dialog = QtWidgets.QDialog()
    # ui = Ui_Dialog()
    # ui.setupUi(Dialog)
    
    widget.show()
    sys.exit(app.exec_())
    print(logged_in)
    