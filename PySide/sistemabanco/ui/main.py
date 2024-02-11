from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from data.ciudad import CiudadData
from data.deposito import DepositoData
from data.transferencia import TransferenciaData
from model.transferencia import DepositoInternacional, Transferencia

from ui.registro import RegistroWindow


class MainWindow():
    def __init__(self):
        self.main = uic.loadUi('ui/main.ui')
        self.initGUI()
        self.main.showMaximized()
        
    def initGUI(self):
        self.main.btnRegistrarTransferencias.triggered.connect(self.abrirRegistro)
        self.main.btnReportarTransferencias.triggered.connect(self.abrirDeposito)
        self.registro = uic.loadUi('ui/registro.ui')
        self.deposito = uic.loadUi('ui/deposito.ui')
        
    def abrirRegistro(self):
        self.registro.btnRegistrar.clicked.connect(self.registrarTransferencia)
        self.registro.show()
        
    
    def abrirDeposito(self):
        self.deposito.btnRegistrar.clicked.connect(self.registarDeposito)
        self.deposito.show()
        self.llenarComboCiudades()
    
    
    
    ## Transferencias 
    def registrarTransferencia(self):
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
            transferencia = Transferencia(
                tipo=self.registro.cbTipo.currentText(),
                documento=self.registro.txtDocumento.text(),
                motivo=self.registro.cbMotivo.currentText(),
                monto=self.registro.txtMonto.text(),
                internacional=self.registro.checkInternacional.isChecked(),
                dolares = self.registro.checkDolares.isChecked()
                
            )
            objData = TransferenciaData()
            mBox = QMessageBox()
            if objData.registrar(info=transferencia):
                mBox.setText('Transferencia registrada')
            else:
                mBox.setText('Transferencia no registrada')
            mBox.exec()
            self.limpiarCamposTransferencias()
    
    
    def limpiarCamposTransferencias(self):
        self.registro.cbTipo.setCurrentIndex(0)   
        self.registro.cbMotivo.setCurrentIndex(0)   
        self.registro.txtDocumento.setText('')   
        self.registro.txtMonto.setText('')
        self.registro.checkInternacional.setChecked(False)
        self.registro.checkDolares.setChecked(False)
        self.registro.txtDocumento.setFocus()
        
    
    #### Depositos
    def llenarComboCiudades(self):
        objData = CiudadData()
        datos = objData.listCiudades()
        
        for item in datos:
            self.deposito.cbLugar.addItem(item[1])
    
    
    def validarCamposObligatorios(self):
        mBox = QMessageBox()
        if (not self.deposito.txtDocumento.text() 
            or not self.deposito.txtPrimerNombre.text()
            or not self.deposito.txtSegundoNombre.text()
            or not self.deposito.txtPrimerApellido.text()
            or not self.deposito.txtMonto.text()
            or self.deposito.cbMotivo.currentText() == '--- Seleccione una opcion'
            or self.deposito.cbSexo.currentText() == '--- Seleccione una opcion'
            ):
            return False
        else:
            return True
        
    
    def registarDeposito(self):
        mBox = QMessageBox()
        if self.validarCamposObligatorios():
            mBox.setText('Debe llenar los campos')
        else:
            fechaN = self.deposito.txtFecha.date().toPyDate()
            deposito = DepositoInternacional(
            tipo=self.deposito.cbTipo.currentText(),
            documento=self.deposito.txtDocumento.text(),
            motivo=self.deposito.cbMotivo.currentText(),
            monto=self.deposito.txtMonto.text(),
            nombre1=self.deposito.txtPrimerNombre.text(),
            nombre2=self.deposito.txtSegundoNombre.text(),
            apellido1=self.deposito.txtPrimerApellido.text(),  # Corrected from previous version
            apellido2=self.deposito.txtSegundoApellido.text(),
            sexo=self.deposito.cbSexo.currentText(),  # Corrected from previous version
            fechaNacimiento=fechaN,
            lugarNacimi=self.deposito.cbLugar.currentText(), # Corrected from previous version
            terminos=self.deposito.checkTerminos.isChecked() # Corrected from previous version
        )

        objData = DepositoData()
        if objData.registrar(deposito):
            mBox.setText('Deposito registrada')
        else:
            mBox.setText('Deposito no registrada')
        mBox.exec()