from datetime import datetime
import conexion as con
from model.transferencia import DepositoInternacional

class DepositoData:

    def __init__(self):
        """
        Crea la tabla "deposito" si no existe.
        """
        try:
            self.db = con.Conexion().conectar()
            self.cursor = self.db.cursor()

            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS deposito (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tipo TEXT, 
                    documento TEXT, 
                    motivo TEXT, 
                    monto REAL, 
                    internacional INTEGER DEFAULT 0,
                    dolares INTEGER DEFAULT 0,
                    fecha_nacimiento TEXT,
                    pnombre TEXT,
                    snombre TEXT,
                    papellido TEXT,
                    sapellido TEXT,
                    sexo TEXT,
                    ciudad TEXT,
                    terminos INTEGER DEFAULT 0
                )
            """)

            self.db.commit()
        except Exception as e:
            print(f"Error al crear la tabla: {e}")
        finally:
            self.cursor.close()
            self.db.close()

    def registrar(self, deposito: DepositoInternacional) -> bool:
        """
        Registra un nuevo depósito internacional en la base de datos.

        Args:
            deposito (DepositoInternacional): Objeto con la información del depósito.

        Returns:
            bool: True si el registro fue exitoso, False en caso contrario.
        """
        try:
            fecha = datetime.datetime.now().strftime('%d/%m/%y %H:%M:%S')

            self.db = con.Conexion().conectar()
            self.cursor = self.db.cursor()

            self.cursor.execute("""
                INSERT INTO deposito (
                    tipo, 
                    documento, 
                    motivo, 
                    monto, 
                    dolares,
                    internacional,
                    pnombre,
                    snombre,
                    papellido,
                    sapellido,
                    sexo,
                    fecha_nacimiento,
                    ciudad,
                    terminos
                ) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                deposito._tipo,
                deposito._documento,
                deposito._motivo,
                deposito._monto,
                deposito._dolares,
                deposito._internacional,
                deposito._nombre1,
                deposito._nombre2,
                deposito._apellido1,
                deposito._apellido2,
                deposito._sexo,
                deposito._fechaNacimiento,
                deposito._lugarNacimi,
                deposito._terminos,
            ))

            self.db.commit()

            return self.cursor.rowcount == 1
        except Exception as e:
            print(f"Error al registrar el depósito: {e}")
            return False
        finally:
            self.cursor.close()
            self.db.close()

