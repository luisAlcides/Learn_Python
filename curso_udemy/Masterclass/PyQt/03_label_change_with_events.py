from PyQt6.QtWidgets import QWidget


class Window(QWidget):
    def __init__(self):
        super.__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My first Application')
        self.setGeometry(0,0,400,400)