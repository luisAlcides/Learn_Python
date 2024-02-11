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
                    );

                    
                '''
            sql_create_table_transferencias = '''
                CREATE TABLE IF NOT EXISTS transferencias(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        tipo TEXT,
                        documento TEXT,
                        motivo TEXT,
                        monto REAL,
                        internacional INTEGER DEFAULT 0,
                        dolares INTEGER DEFAULT 0,
                        verificado INTEGER DEFAULT 0,
                        fecha_registro TEXT
                    )
            '''
            cur = self.con.cursor()
            cur.execute(sql_create_table1)
            cur.execute(sql_create_table_transferencias)
            cur.close()
            self.crearAdminIfNotExists()
        except Exception as e:
            print('Hubo un error al crear la tabla usuarios', e)
            
    def crearAdmin(self):
        try:
            sql_insert ='''
                    INSERT INTO usuarios(nombre, usuario, clave) values(?, ?, ?)'''
            cur = self.con.cursor()
            cur.execute(sql_insert, ('administrador', 'admin', 'admin'))
            self.con.commit() 
            cur.close()  # Cerrar el cursor
        except Exception as e:
            print('Ha ocurrido un error al crear el admin', e)
    
    def crearAdminIfNotExists(self):
        # Check if an admin exists
        cur = self.con.cursor()
        exists = cur.execute("SELECT 1 FROM usuarios WHERE usuario='admin'").fetchone()
        cur.close()

        if exists is None:
            # Create admin if not found
            self.crearAdmin()
    
    
            
    def conectar(self):
        try:
            self.con = sqlite3.connect('banco.db')
            self.crearAdminIfNotExists()  # Check and create admin if needed
            return self.con
        except Exception as e:
            print('No se pudo conectar ', e)
