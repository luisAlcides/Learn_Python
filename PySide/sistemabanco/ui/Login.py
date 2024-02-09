from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox

from data.usuario import UsuarioData
from model.usuario import Usuario
from ui.main import MainWindow


class Login():
    def __init__(self):
        self.login = uic.loadUi('ui/Login.ui')
        self.initGUI()
        self.login.lblMensaje.setText('')
        self.login.show()
        
        
    def ingresar(self):
        if len(self.login.txtUsuario.text()) < 2:
            self.login.lblMensaje.setText('Ingrese un usuario valido')
            self.login.txtUsuario.setFocus()
        elif len(self.login.txtClave.text()) < 5:
            self.login.lblMensaje.setText('Ingrese una contrasena mas segura')
            self.login.txtClave.setFocus()
        else:
            self.login.lblMensaje.setText('')
            usu = Usuario(usuario=self.login.txtUsuario.text(), clave=self.login.txtClave.text())
            usuData = UsuarioData()
            res = usuData.login(usu)
            if res:
                self.main = MainWindow()
                self.login.close()
            else:
                self.login.lblMensaje.setText('Datos incorrectos')
                
                
    def initGUI(self):
        self.login.btnAcceder.clicked.connect(self.ingresar)