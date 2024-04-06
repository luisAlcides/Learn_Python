import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QStyleFactory, QLabel, QVBoxLayout, QWidget


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 700, 500)
        label = QLabel('<h1><font color="red">This is a label</h1>', self)
        label.resize(200, 50)
        label.setStyleSheet('background-color:red')
        layout = QVBoxLayout()
        layout.addWidget(label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())