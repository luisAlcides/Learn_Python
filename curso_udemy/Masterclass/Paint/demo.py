import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel


class Canvas(QLabel):
    def __init__(self):
        super().__init__()
        self.pixmap = None
        self.initUI()

    def initUI(self):
        self.pixmap = QPixmap(600, 600)
        self.pixmap.fill(Qt.GlobalColor.white)
        self.setPixmap(self.pixmap)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        mouse_position = event.pos()
        print(mouse_position)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            print('Left click at position')

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            print('Mouse released at position ' + str(event.pos()))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setMinimumSize(600, 600)
        self.setWindowTitle('Paint App')

        # Creating a canvas
        canvas = Canvas()
        self.setCentralWidget(canvas)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
