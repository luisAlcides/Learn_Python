import sys

from PyQt6.QtWidgets import QWidget, QApplication, QTableWidget, QVBoxLayout, QTabWidget, QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 700, 500)
        # Creating a tab widget
        tab_widget = QTabWidget()

        # Create tabs
        tab1 = QWidget()
        tab2 = QWidget()

        # Adding above tabs to the tab widget
        tab_widget.addTab(tab1, 'tab1')
        tab_widget.addTab(tab2, 'tab2')

        # create widget to be added to tabs
        button1 = QPushButton('Buttn1')
        button2 = QPushButton('Buttn2')

        # Creating laout for tab1 and tab2
        layout1 = QVBoxLayout()
        layout1.addWidget(button1)
        layout2 = QVBoxLayout()
        layout2.addWidget(button2)

        # Setting the tab layout
        tab1.setLayout(layout1)
        tab2.setLayout(layout2)

        # Add the above tab widget to the main window
        layout = QVBoxLayout(self)
        layout.addWidget(tab_widget)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
