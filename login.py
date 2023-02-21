import sys
from PySide6 import QtWidgets, QtGui
from main import *

class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        global widgets  
        widgets = self.ui
        
        
        
    def initUI(self):
        widgets.txt_name = QtWidgets.QLineEdit(self)
        widgets.txt_password = QtWidgets.QLineEdit(self)
        widgets.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        widgets.btn_login = QtWidgets.QPushButton("Login", self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(QtWidgets.QLabel("Username:"))
        layout.addWidget(self.txt_name)
        layout.addWidget(QtWidgets.QLabel("Password:"))
        layout.addWidget(self.txt_password)
        layout.addWidget(self.btn_login)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        self.setWindowTitle("Login")
        self.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginWindow()
    sys.exit(app.exec_())
