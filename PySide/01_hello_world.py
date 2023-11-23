import sys

from PySide6.QtWidgets import QApplication, QWidget

app = QApplication()

window = QWidget()
window.setWindowTitle('Hola mundo con pyside6')
window.resize(600, 400)
window.show()

sys.exit(app.exec())
