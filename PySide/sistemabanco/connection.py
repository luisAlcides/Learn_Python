import sqlite3

class Connection():
    def __init__(self):
        try:
            self.con = sqlite3.connect('banco.db')
            self.createtables()
        except Exception as ex:
            print(ex)
    
    def createtables(self):
        try:
            sql_create_table1 = '''
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    username TEXT UNIQUE,
                    password TEXT
                )
            '''
            cursor = self.con.cursor()
            cursor.execute(sql_create_table1)
            cursor.close()
            self.createAdmin()
        except Exception as ex:
            print(ex)
            
    def createAdmin(self):
        try:
            sql_insert = '''
                INSERT INTO users(name, username, password) values('{}', '{}', '{}')
            '''.format('Administrador', 'admin', 'admin')
            cursor = self.con.cursor()
            cursor.execute(sql_insert)
            self.con.commit()
            cursor.close()
        except Exception as ex:
            print('Ya se creo el usuario admin ',ex)

