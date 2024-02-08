import sqlite3

class Conexion():
    def __init__(self):
        try:
            self.con = sqlite3.connect('banco.db')
            self.creartablas()
        except Exception as ex:
            print(ex)

    def creartablas(self):
        try:
            sql_create_table1 = '''
                    CREATE TABLE IF NOT EXISTS usuarios(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT,
                        usuario TEXT UNIQUE,
                        clave TEXT
                    )
                '''
            cur = self.con.cursor()
            cur.execute(sql_create_table1)  # Ejecutar la consulta
            cur.close()
            self.crearAdmin()
        except Exception as e:
            print('Hubo un error al crear la tabla usuarios', e)
            
    def crearAdmin(self):
        try:
            sql_insert ='''
                    INSERT INTO usuarios(nombre, usuario, clave) values('{}', '{}', '{}')'''.format('administrador', 'admin', 'admin')
            cur = self.con.cursor()
            cur.execute(sql_insert)
            self.con.commit() 
            cur.close()  # Cerrar el cursor
        except Exception as e:
            print('Ha ocurrido un error al crear el admin', e)
            
            
