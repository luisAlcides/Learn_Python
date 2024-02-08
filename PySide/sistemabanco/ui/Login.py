from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox


class Login():
    def __init__(self):
        self.login = uic.loadUi('ui/LoginWindow.ui')
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
            user = UserModel(username=self.login.txtUsuario, password=self.login.txtClave)
            userData = UserData()
            res = userData.Login(userData)
            if res:
                self.login.lblMensaje.setText('Ok')
            else:
                self.login.lblMensaje.setText('Login incorrecto')
            
            
    def initGUI(self):
        self.login.btnAcceder.clicked.connect(self.enter)