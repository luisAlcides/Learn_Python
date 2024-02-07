from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox


class LoginWindow():
    def __init__(self):
        self.login = uic.loadUi('ui/LoginWindow.ui')
        self.login.show()