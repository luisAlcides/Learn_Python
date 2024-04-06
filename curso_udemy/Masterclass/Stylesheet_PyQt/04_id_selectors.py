import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QStyleFactory, QLabel, QVBoxLayout, QWidget, QPushButton

stylesheet = '''
    QLabel#My_label{
        background-color: white;
        color: red;
    }
    QPushButton#My_Button{
                background-color: green;
                padding:5px
            }
    QPushButton#My_Button:pressed{
        background-color:blue;
        padding:5px;
    }
'''


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 700, 500)
        label = QLabel('<h1>This is a label</h1>', self)
        label.resize(200, 50)
        label.setObjectName('My_label')
        button = QPushButton('Click here')
        button.setObjectName('My_Button')
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


app = QApplication(sys.argv)
app.setStyleSheet(stylesheet)
window = Window()
window.show()
sys.exit(app.exec())
