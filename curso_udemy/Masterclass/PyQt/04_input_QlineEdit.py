import sys

from PyQt6.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QLineEdit


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.count = 0
        self.setWindowTitle('My first Application')
        self.setGeometry(0,0,300,200)

        # adding label to dispaly
        label = QLabel(self)
        label.setText('Enter your name')
        label.move(60, 10)

        self.name = QLineEdit(self)
        self.name.resize(200, 20)
        self.name.move(60, 50)

        button = QPushButton(self)
        button.setText('Click')
        button.move(200, 80)
        button.clicked.connect(self.buttonClicked)

        self.result_label = QLabel(self)
        self.result_label.setFixedSize(150, 20)
        self.result_label.move(60, 120)
    def buttonClicked(self):
        self.result_label.setText(self.name.text())


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
