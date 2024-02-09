from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox

from ui.registro import RegistroWindow


class MainWindow():
    def __init__(self):
        self.main = uic.loadUi('ui/main.ui')
        self.initGUI()
        self.main.showMaximized()
        
    def initGUI(self):
        self.main.btnRegistrarTransferencias.triggered.connect(self.abrirRegistro)
        self.registro = uic.loadUi('ui/registro.ui')
        
    def abrirRegistro(self):
        self.registro.btnRegistrar.clicked.connect(self.registrarTransaccion)
        self.registro.show()
    
    def registrarTransaccion(self):
        if self.registro.cbTipo.currentText() == '--- Seleccione una opcion':
            mBox = QMessageBox()
            mBox.setText('Debes seleccionar el tipo de documento')
            mBox.exec()
            self.registro.cbTipo.setFocus()
        elif len(self.registro.txtDocumento.text()) < 3:
            mBox = QMessageBox()
            mBox.setText('Debe ingresar un documento valido')
            mBox.exec()
            self.registro.txtDocumento.setFocus()
            
        elif self.registro.cbMotivo.currentText() == '--- Seleccione una opcion':
            mBox = QMessageBox()
            mBox.setText('Debes seleccionar el motivo')
            mBox.exec()
            self.registro.cbMotivo.setFocus()
            
        elif not self.registro.txtMonto.text().isnumeric():
            mBox = QMessageBox()
            mBox.setText('Debe ingresar un monto valido')
            mBox.exec()
            self.registro.txtMonto.setFocus()
        
        else:
            print('Trans', str(self.registro.checkInternacional.isChecked()))
            print('Dolar', str(self.registro.checkDolares.isChecked()))
    
        