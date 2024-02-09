import conexion as con
from model.usuario import Usuario

class UsuarioData():
    def login(self, usuario):
        self.db = con.Conexion().conectar()
        self.cursor = self.db.cursor()
        res = self.cursor.execute("SELECT * FROM usuarios WHERE usuario=? AND clave=?", (usuario._usuario, usuario._clave))
        fila = res.fetchone()
        if fila:
            usuario = Usuario(usuario=fila[1], clave=fila[2])
            self.cursor.close()
            self.db.close()
            return usuario
        else:
            self.cursor.close()
            self.db.close()
            return None    
    