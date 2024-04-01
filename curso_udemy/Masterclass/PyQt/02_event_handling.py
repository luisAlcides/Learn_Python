from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton
import sys
from PyQt6.QtGui import QPixmap, QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My first PyQtWindow')
        self.setGeometry(0, 0, 400, 400)
    # new code added to create button
        button = QPushButton(self)
        button.setText('Click here')
        button.move(100, 200)
        button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        print('Hello world')


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
