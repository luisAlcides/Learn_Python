import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Nested Layout')
        self.setGeometry(0, 0, 400, 150)

        button1 = QPushButton('Button 1', self)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
