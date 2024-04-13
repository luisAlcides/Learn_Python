import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QTableWidget, QTableWidgetItem


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('databases')
        self.setGeometry(0, 0, 700, 500)

        people = [
            {'First Name': 'John', 'Last Name': 'Dow', 'Age': 21},
            {'First Name': 'Rob', 'Last Name': 'DTyson', 'Age': 21},
            {'First Name': 'Bob', 'Last Name': 'Ford', 'Age': 23},
        ]

        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(len(people))
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(people[0].keys())

        row = 0
        for person in people:
            self.table_widget.setItem(row, 0, QTableWidgetItem(person['First Name']))
            self.table_widget.setItem(row, 1, QTableWidgetItem(person['Last Name']))
            self.table_widget.setItem(row, 2, QTableWidgetItem(str(person['Age'])))
            row += 1

        self.setCentralWidget(self.table_widget)




app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())