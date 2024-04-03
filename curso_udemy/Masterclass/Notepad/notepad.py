import sys

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QApplication, QTextEdit, QMenuBar, QMenu, QFileDialog


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Notepad')
        self.setGeometry(100, 100, 800, 600)

        self.set_current_file = None

        self.edit_field = QTextEdit(self)
        self.setCentralWidget(self.edit_field)

        # create a menubar
        menubar = QMenuBar(self)
        self.setMenuBar(menubar)

        # creating file menu
        fileMenu = QMenu('File', self)
        menubar.addMenu(fileMenu)

        # Create actions
        new_action = QAction('New', self)
        fileMenu.addAction(new_action)
        new_action.triggered.connect(self.new_file)

        open_action = QAction('open', self)
        fileMenu.addAction(open_action)
        open_action.triggered.connect(self.open_file)

        save_action = QAction('Save', self)
        fileMenu.addAction(save_action)
        save_action.triggered.connect(self.save_file)

        save_as_action = QAction('Save As', self)
        fileMenu.addAction(save_as_action)
        save_as_action.triggered.connect(self.save_as_file)

        # Creating the edit menu
        editmenu = QMenu('Edit', self)
        menubar.addMenu(editmenu)

        undo_action = QAction('Undo', self)
        editmenu.addAction(undo_action)
        undo_action.triggered.connect(self.edit_field.undo)

        redo_action = QAction('Redo', self)
        editmenu.addAction(redo_action)
        redo_action.triggered.connect(self.edit_field.redo)

        cut_action = QAction('Cut', self)
        editmenu.addAction(cut_action)
        cut_action.triggered.connect(self.edit_field.cut)

        paste_action = QAction('Paste', self)
        editmenu.addAction(paste_action)
        paste_action.triggered.connect(self.edit_field.paste)

        copy_action = QAction('Copy', self)
        editmenu.addAction(copy_action)
        copy_action.triggered.connect(self.edit_field.copy)


    def new_file(self):
        self.edit_field.clear()
        self.set_current_file = None

    def open_file(self):
        file_path,_ = QFileDialog.getOpenFileName(self, 'Open File', '', 'All Files(*);; Python File (*.py);; Text File (*.txt))')
        with open(file_path, 'r') as file:
            text = file.read()
            self.edit_field.setText(text)

    def save_file(self):
        if self.set_current_file:
            with open(self.set_current_file, 'w') as file:
                file.write(self.edit_field.toPlainText())
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'All Files(*);; Python File (*.py);; Text File (*.txt))')
        if file_path:
            with open(file_path, 'w') as file:
                text = self.edit_field.toPlainText()
                file.write(text)
            self.set_current_file = file_path


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
