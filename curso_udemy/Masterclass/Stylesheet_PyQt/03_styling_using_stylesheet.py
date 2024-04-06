import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QStyleFactory, QLabel, QVBoxLayout, QWidget, QPushButton


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 700, 500)
        label = QLabel('<h1>This is a label</h1>', self)
        label.resize(200, 50)
        label.setStyleSheet('''background-color:red;
                                color:white;
                                margin-top:100px;
                                margin-bottom:100px;
                                margin-left:100px;
                                margin-right:100px;
                                ''')
        button = QPushButton('Click here')
        button.setStyleSheet('''
            QPushButton{
                background-color: green;
                padding:5px
            }
            QPushButton:pressed{
                background-color:blue;
                padding:5px;
            }
        ''')
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())