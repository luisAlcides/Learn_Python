import sys

from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QCheckBox


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('two numbers')
        self.setGeometry(0, 0, 400, 150)

        sugar_checkbox = QCheckBox(self)
        sugar_checkbox.setText('Sugar')
        sugar_checkbox.move(20, 40)
        sugar_checkbox.toggled.connect(self.sugar_checked)

    def sugar_checked(self, checked):
        if checked:
            print('Sugar added')
        else:
            print('Sugar not added')


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
