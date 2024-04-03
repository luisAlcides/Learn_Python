import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QFormLayout, QWidget, QComboBox, QPushButton, \
    QTextEdit


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QForm')
        self.setGeometry(0, 0, 400, 150)

        form_layout = QFormLayout()

        self.name_edit = QLineEdit()
        self.email_edit = QLineEdit()
        self.phone_edit = QLineEdit()

        self.subject_combo = QComboBox()
        self.subject_combo.addItems(['Select Subject', 'Personal', 'Bussiness', 'Other'])

        self.message_edit = QTextEdit()

        submit_button = QPushButton('Submit')
        submit_button.clicked.connect(self.submitClicked)

        form_layout.addRow(QLabel('Name:'), self.name_edit)
        form_layout.addRow(QLabel('Email: '), self.email_edit)
        form_layout.addRow(QLabel('Phone: '), self.phone_edit)
        form_layout.addRow(QLabel('Subject'), self.subject_combo)
        form_layout.addRow(QLabel('Message'), self.message_edit)
        form_layout.addRow(submit_button)

        central_widget = QWidget()
        central_widget.setLayout(form_layout)
        self.setCentralWidget(central_widget)
    def submitClicked(self):
        name = self.name_edit.text()
        email = self.email_edit.text()
        phone = self.phone_edit.text()
        subject = self.subject_combo.currentText()
        message = self.message_edit.toPlainText()

        print(f'Name: {name} \nEmail: {email} \nPhone: {phone} \n'
              f'Subject: {subject} \nMessage: {message}')

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
