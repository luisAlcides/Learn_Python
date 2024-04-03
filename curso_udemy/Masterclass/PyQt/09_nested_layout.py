import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QWidget


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Nested Layout')
        self.setGeometry(0, 0, 400, 150)

        button1 = QPushButton('Button 1', self)
        button2 = QPushButton('Button 2', self)
        button3 = QPushButton('Button 3', self)
        button4 = QPushButton('Button 4', self)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(button1)
        hbox1.addWidget(button2)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(button3)
        hbox2.addWidget(button4)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
