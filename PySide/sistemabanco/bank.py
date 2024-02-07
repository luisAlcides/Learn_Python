from PyQt6.QtWidgets import QApplication

from ui.LoginWindow import LoginWindow


class Bank():
    def __init__(self):
        self.app = QApplication([])
        self.login = LoginWindow()
        self.app.exec()