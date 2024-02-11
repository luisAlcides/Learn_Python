
class Transferencia():
    def __init__(self, tipo:str, documento:str, motivo:str, monto:float, internacional:bool, dolares:bool):
        self._tipo = tipo
        self._documento = documento
        self._motivo = motivo
        self._monto = monto
        self._internacional = internacional
        self._dolares = dolares
        

class DepositoInternacional():
    def __init__(
        self,
        tipo,
        documento,
        motivo,
        monto,
        nombre1,
        nombre2,
        apellido1,
        apellido2,
        sexo,
        fechaNacimiento,
        lugarNacimi,
        terminos
        
    ):
        self._tipo = tipo
        self._documento = documento,
        self._motivo = motivo
        self._monto = monto
        self._dolares = True
        self._internacional = True
        self._nombre1 = nombre1
        self._nombre2 = nombre2
        self._apellido1 = apellido1
        self._apellido2 = apellido2
        self._sexo = sexo
        self._fechaNacimiento = fechaNacimiento
        self._lugarNacimi = lugarNacimi
        self._terminos = terminos