import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QFormLayout, QWidget


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('QForm')
        self.setGeometry(0, 0, 400, 150)

        label1 = QLabel('Label 1')
        name_edit = QLineEdit(self)

        label2 = QLabel('Label 2')
        age_edit = QLineEdit(self)

        form_layout = QFormLayout()
        form_layout.addRow(label1, name_edit)
        form_layout.addRow(label2, age_edit)

        central_widget = QWidget()
        central_widget.setLayout(form_layout)
        self.setCentralWidget(central_widget)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())