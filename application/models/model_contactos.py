from application.config.database import Database


class Contactos():

    db = Database()
    mysql = db.get_connection()

    def __init__(self):
        pass

    def get_contactos(self):
        cur = self.mysql.connection.cursor()
        cur.execute('''SELECT * FROM  contactos''')
        data = cur.fetchall()
        return data

    def add_contacto(self, nombre, telefono, email):
        try:
            cur = self.mysql.connection.cursor()
            cur.execute('INSERT INTO contactos (nombre, telefono, email) VALUES ( %s, %s, %s)', (nombre, telefono, email)) #preparamos la consulta con el metodo execute del metodo con 
            self.mysql.connection.commit()
        except:
            print("Error 001 function add_contacto")

    def delete_contactos(self, id):
        try:
            cur = self.mysql.connection.cursor()
            sql = "DELETE FROM contactos WHERE id = {id}"
            cur.execute(sql.format(id = id))
            self.mysql.connection.commit()
            print(cur.rowcount, "record(s) deleted")
            return cur.rowcount
        except:
            print("Error 002 function delete_contacto")


    def get_by_id(self, id: int)-> tuple:
        try:
            cur = self.mysql.connection.cursor()
            sql = "SELECT * FROM contactos WHERE id = {id}"
            cur.execute(sql.format(id = id))
            data = cur.fetchall()
            return data
        except:
            print('Error function det_by_id')

            
    def update_contacto(self, id: int , nombre: str, telefono: int, email: str) -> int:
        try:
            cur = self.mysql.connection.cursor()
            sql = 'UPDATE contactos SET nombre = %s, telefono = %s, email = %s WHERE id = %s'
            values = (nombre, telefono, email, id)
            cur.execute(sql, values)
            self.mysql.connection.commit()
            print(cur.rowcount, "record(s) updated")
            return cur.rowcount
        except:
            print('Error function update_contacto')
            
            


        