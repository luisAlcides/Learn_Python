import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QMessageBox


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Message Box')
        self.setGeometry(0, 0, 400, 150)

        button = QPushButton('Show message box', self)
        button.move(200, 40)
        button.setGeometry(150, 80, 200, 40)
        button.clicked.connect(self.show_message_box)

    def show_message_box(self):
        msg = QMessageBox()
        msg.setWindowTitle('Message box title')
        msg.setText('This is a simple QMessageBox')
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        msg.setDefaultButton(QMessageBox.StandardButton.Ok)
        result = msg.exec()


        if result == QMessageBox.StandardButton.Ok:
            print('Ok button is clicked')
        else:
            print('Cancel button is clicked')


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
