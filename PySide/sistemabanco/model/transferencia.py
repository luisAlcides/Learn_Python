
class Transferencia():
    def __init__(self, tipo:str, documento:str, motivo:str, monto:float, internacional:bool, dolares:bool):
        self._tipo = tipo
        self._documento = documento
        self._motivo = motivo
        self._monto = monto
        self._internacional = internacional
        self._dolares = dolares