import sys
from PyQt6.QtWidgets import QWidget, QApplication


class SimpleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Simple window')
        self.setGeometry(400, 400, 400, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    window = SimpleWindow()
    app.exec()
    sys.exit(app.exec())

