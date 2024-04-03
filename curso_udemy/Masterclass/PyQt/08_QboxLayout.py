import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QHBoxLayout, QWidget, QVBoxLayout


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QBoxLayout')
        self.setGeometry(0, 0, 400, 150)

        label = QLabel('Name')
        name = QLineEdit()
        button = QPushButton('Add')

        # layout = QHBoxLayout()
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(name)
        layout.addWidget(button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
