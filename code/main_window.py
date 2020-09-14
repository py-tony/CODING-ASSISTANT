from PyQt5 import QtCore, QtGui, QtWidgets
from main_window_qt import Ui_CODE_ASSISTANT 



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CODE_ASSISTANT = QtWidgets.QMainWindow()
    ui = Ui_CODE_ASSISTANT()
    ui.setupUi(CODE_ASSISTANT)
    CODE_ASSISTANT.show()
    sys.exit(app.exec_())
