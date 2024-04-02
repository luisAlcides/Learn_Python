import sys

from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QLineEdit


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('two numbers')
        self.setGeometry(0, 0, 400, 150)

        num1_label = QLabel('Enter first number', self)
        num1_label.resize(200, 20)
        num1_label.move(20, 20)
        num1_input = QLineEdit(self)
        num1_input.move(200, 20)


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
