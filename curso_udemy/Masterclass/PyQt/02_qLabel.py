from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QApplication, QLabel
import sys


class Label(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Label')
        self.setGeometry(400, 400, 400, 300)

        label = QLabel(self)
        label.setText('Hello world')
        label.move(50, 50)

        with open('car.png'):
            image_label = QLabel(self)
            pixmanp = QPixmap('car.png')
            image_label.setPixmap(pixmanp)
            image_label.move(50, 100)

        self.show()



app = QApplication([])
window = Label()
app.exec()
