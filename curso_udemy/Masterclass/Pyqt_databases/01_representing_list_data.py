import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QListWidget, QListWidgetItem, QHBoxLayout, QWidget


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('databases')
        self.setGeometry(0, 0, 700, 500)
        fruits = ['Apple', 'Mango', 'Orange', 'Banana', 'Pineapple']

        self.listWidget = QListWidget()
        self.listWidget.setAlternatingRowColors(True)

        for fruit in fruits:
            listItem = QListWidgetItem()
            listItem.setText(fruit)
            self.listWidget.addItem(listItem)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.listWidget)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())