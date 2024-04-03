import sys

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QApplication

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('QMenuBar')
        self.setGeometry(0, 0, 400, 150)

        # Step 1: Create a menubar
        menubar = self.menuBar()

        # creating the menu items
        file_menu = menubar.addMenu('File')

        self.new_action = QAction("New")

        # adding action to the menu
        file_menu.addAction(self.new_action)

        file_menu.addSeparator()

        #creating another action
        self.exit_action = QAction('Exit')
        file_menu.addAction(self.exit_action)

        # creating a new menu
        edit_menu = menubar.addMenu('Edit')

        self.copy_action = QAction('Copy')
        edit_menu.addAction(self.copy_action)




app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
