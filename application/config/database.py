from application import app
# sfrom flask_mysqldb import MySQL 
import mysql.connector
from flask_mysqldb import MySQL


class Database:
  
  
  app.config['MYSQL_HOST'] = '127.0.0.1'
  app.config['MYSQL_USER'] = 'root'
  app.config['MYSQL_PASSWORD'] = 'oscarescamilla26'
  app.config['MYSQL_DB'] = 'flask_crud'
  mysql = MySQL(app)
  
  def __init__(self):
    pass

  def get_connection(self):
    return self.mysql







  











"""
mycursor.execute("SELECT * FROM contactos")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


keys = {
    "host": "localhost",
    "password": "oscarescamilla26",
    "user": "root",
    "database": "flask_crud"
}

app.config['MYSQL_HOST'] = keys['host']
app.config['MYSQL_USER'] = keys['user']
app.config['MYSQL_PASSWORD'] = keys['password']
app.config['MYSQL_DB'] = keys['database']

app.secret_key = 'mysecret'

mysql = MySQL(app)  

#con = mysql.connection.cursor() #instanciamos la conexion
"""
