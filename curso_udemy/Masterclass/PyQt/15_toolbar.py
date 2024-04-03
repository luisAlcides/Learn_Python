import sys

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QApplication


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()



    def initUI(self):
        self.setWindowTitle('Toolbar')
        self.setGeometry(0, 0, 400, 150)

        self.toolbar = self.addToolBar('Toolbar')
        self.toolbar.addAction('New')
        self.open_action = QAction('Open')
        self.toolbar.addAction(self.open_action)



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())