import datetime
import conexion as con
from model.transferencia import Transferencia

class TransferenciaData():
    
    def registrar(self, info:Transferencia):
        fecha = datetime.datetime.now().strftime('%d/%m/%y %H:%M:%S')
        self.db = con.Conexion().conectar()
        self.cursor = self.db.cursor()
        self.cursor.execute('''
                            INSERT INTO 
                            transferencias (
                                tipo, 
                                documento, 
                                motivo, 
                                monto, 
                                internacional,
                                dolares,
                                verificado,
                                fecha_registro 
                                ) 
                            values(?,?,?,?,?,?,?,?)
                            ''', (info._tipo, 
                                info._documento, 
                                info._motivo, 
                                info._monto, 
                                info._internacional,
                                info._dolares,
                                False,
                                fecha
                                )
                            )
        self.db.commit()
        if self.cursor.rowcount == 1:
            return True
        else:
            return False