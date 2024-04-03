import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QComboBox, QLabel, QFormLayout, QStackedLayout, QWidget, \
    QVBoxLayout


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QStackedLayout')
        self.setGeometry(0, 0, 400, 150)

        combo_box = QComboBox(self)
        combo_box.addItems(['Label', 'Form'])
        combo_box.activated.connect(self.changePage)

        # creating page 1
        label = QLabel('This is label page 1')

        # creating page 2
        form = QFormLayout()
        form.addRow('', QLabel('This is a form page'))
        page2_container = QWidget()
        page2_container.setLayout(form)

        # Creating a stacked layout
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(label)
        self.stacked_layout.addWidget(page2_container)

        main_layout = QVBoxLayout()
        main_layout.addWidget(combo_box)
        main_layout.addLayout(self.stacked_layout)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def changePage(self, index):
        self.stacked_layout.setCurrentIndex(index)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
