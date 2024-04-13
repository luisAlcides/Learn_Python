import sqlite3

from PyQt6.QtWidgets import QWidget, QApplication, QApplication, QLabel, QMainWindow, QVBoxLayout, QTableWidget, \
    QTableWidgetItem, QLineEdit, QPushButton, QMessageBox
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.products = [
            {'name': 'iPhone', 'price': 600, 'description': 'This is an iPhone'},
            {'name': 'Samsung Galaxy', 'price': 700, 'description': 'This is a Samsung Galaxy phone'},
            {'name': 'Google Pixel', 'price': 800, 'description': 'This is a Google Pixel phone'},
            {'name': 'iPad', 'price': 400, 'description': 'This is an iPad'},
            {'name': 'MacBook Pro', 'price': 1200, 'description': 'This is a MacBook Pro'},
            {'name': 'Dell XPS', 'price': 1000, 'description': 'This is a Dell XPS laptop'},
            {'name': 'Sony PlayStation 5', 'price': 500, 'description': 'This is a Sony PlayStation 5 gaming console'},
            {'name': 'Nintendo Switch', 'price': 300, 'description': 'This is a Nintendo Switch gaming console'},
            {'name': 'Canon EOS Rebel T7i', 'price': 700, 'description': 'This is a Canon EOS Rebel T7i camera'},
            {'name': 'Sony Alpha A7 III', 'price': 2000, 'description': 'This is a Sony Alpha A7 III camera'},
            {'name': 'Bose QuietComfort 35 II', 'price': 300,
             'description': 'This is a Bose QuietComfort 35 II headphones'},
            {'name': 'Apple Watch Series 7', 'price': 400, 'description': 'This is an Apple Watch Series 7'},
            {'name': 'Samsung 4K QLED TV', 'price': 1500, 'description': 'This is a Samsung 4K QLED TV'},
            {'name': 'LG OLED TV', 'price': 2000, 'description': 'This is an LG OLED TV'},
            {'name': 'Xbox Series X', 'price': 500, 'description': 'This is an Xbox Series X gaming console'},
            {'name': 'PlayStation VR', 'price': 300, 'description': 'This is a PlayStation VR headset'},
            {'name': 'Fitbit Charge 4', 'price': 150, 'description': 'This is a Fitbit Charge 4 fitness tracker'},
            {'name': 'Amazon Echo Dot', 'price': 50, 'description': 'This is an Amazon Echo Dot smart speaker'},
            {'name': 'Google Nest Hub', 'price': 100, 'description': 'This is a Google Nest Hub smart display'},
            {'name': 'Microsoft Surface Laptop 4', 'price': 1000, 'description': 'This is a Microsoft Surface Laptop 4'}
        ]

        sqlite3.connect('products.db')
        self.con = sqlite3.connect('products.db')
        self.create_table()

        self.initUI()

    def create_table(self):
        cursor = self.con.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price INTEGER, 
                description TEXT
            )            
        ''')
        self.con.commit()

    def initUI(self):
        self.setWindowTitle('CRUD')
        self.setGeometry(0, 0, 700, 500)


        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.table_widget = QTableWidget(self)
        layout.addWidget(self.table_widget)

        self.table_widget.setRowCount(4)
        self.table_widget.setColumnCount(['ID', 'Name', 'Price', 'Description'])
        self.load_data()

        self.table_widget.setHorizontalHeaderLabels(self.products[0].keys())

        for row, product in enumerate(self.products):
            for col, value in enumerate(product.values()):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)

        self.name_edit = QLineEdit(self)
        self.price_edit = QLineEdit(self)
        self.description_edit = QLineEdit(self)

        layout.addWidget(QLabel('Name:'))
        layout.addWidget(self.name_edit)

        layout.addWidget(QLabel('Price:'))
        layout.addWidget(self.price_edit)

        layout.addWidget(QLabel('Description:'))
        layout.addWidget(self.description_edit)

        add_button = QPushButton('Add Product')
        add_button.clicked.connect(self.add_product)

        delete_button = QPushButton('Delete Product', self)
        delete_button.clicked.connect(self.delete_product)

        update_button = QPushButton('Update Product', self)
        update_button.clicked.connect(self.update_product)

        layout.addWidget(add_button)
        layout.addWidget(delete_button)
        layout.addWidget(update_button)

    def update_product(self):
        current_row = self.table_widget.currentRow()
        if current_row < 0 or current_row >= self.table_widget.rowCount():
            return QMessageBox.warning(self, 'No row selected')

        name = self.name_edit.text().strip()
        price = self.price_edit.text().strip()
        description = self.description_edit.text().strip()

        updated_product = {'name': name, 'price': price, 'description': description}
        self.products[current_row] = updated_product

        for col, value in enumerate(updated_product.values()):
            item = QTableWidgetItem(str(value))
            self.table_widget.setItem(current_row, col, item)

    def delete_product(self):
        current_row = self.table_widget.currentRow()
        if current_row < 0 or current_row >= self.table_widget.rowCount():
            return QMessageBox.warning(self, 'No Row selected')

        mensaje = QMessageBox()
        mensaje.setWindowTitle('Eliminar Producto')
        mensaje.setText('¿Desea eliminar este producto?')

        # Establecer los botones y sus textos
        mensaje.addButton(QMessageBox.StandardButton.Yes)
        mensaje.addButton(QMessageBox.StandardButton.No)
        mensaje.button(QMessageBox.StandardButton.Yes).setText('Sí')
        mensaje.button(QMessageBox.StandardButton.No).setText('No')

        # Mostrar el cuadro de diálogo y obtener la respuesta del usuario
        button = mensaje.exec()

        if button == QMessageBox.StandardButton.Yes:
            self.table_widget.removeRow(current_row)
            del self.products[current_row]

    def add_product(self):
        name = self.name_edit.text().strip()
        price = self.price_edit.text().strip()
        description = self.description_edit.text().strip()

        cursor = self.con.cursor()
        cursor.execute('''
            INSERT INTO products (name, price, description) VALUES(?,?,?)
        ''', (name, price, description,))
        self.con.commit()

        self.name_edit.clear()
        self.price_edit.clear()
        self.description_edit.clear()

    def load_data(self):
        cursor = self.con.cursor()
        cursor.execute('''SELECT * FROM products''')
        products = cursor.fetchall()

        self.table_widget.setRowCount(len(products))

        for row, product in enumerate(products):
            for col, value in enumerate(product):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
