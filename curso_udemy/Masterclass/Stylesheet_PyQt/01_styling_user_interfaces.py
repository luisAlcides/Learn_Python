import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QStyleFactory


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 700, 500)



app = QApplication(sys.argv)
window = Window()
print(QStyleFactory.keys())
print(app.style().name())
window.show()
sys.exit(app.exec())