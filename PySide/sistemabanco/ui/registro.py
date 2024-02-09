from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox


class RegistroWindow():
    def __init__(self):
        self.v = uic.loadUi('ui/registro.ui')
        self.v.show()
        
    
