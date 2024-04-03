import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QGridLayout, QWidget


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('QGridLayout')
        self.setGeometry(0, 0, 400, 150)

        label1 = QLabel('Label 1')
        label2 = QLabel('Label 2')
        label3 = QLabel('Label 3')

        button1 = QPushButton('Button 1')
        button2 = QPushButton('Button 2')
        button3 = QPushButton('Button 3')

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(button1, 0, 1)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(button2, 1, 1)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(button3, 2, 1)
        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())