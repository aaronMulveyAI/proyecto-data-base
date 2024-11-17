import datetime
import hashlib
from usuarios import conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()
        
        # Cifrar contraseña
        cifrado = hashlib.sha3_256()
        cifrado.update(self.password.encode('utf8'))
        
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos,
                   self.email, cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result

    def identificar(self):
        
        # Consulta para sabes si existe usuario
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        
        # Cifrar contraseña
        cifrado = hashlib.sha3_256()
        cifrado.update(self.password.encode('utf8'))
        
        usuario = (self.email, cifrado.hexdigest())
        
        # Datos para la consulta 
        cursor.execute(sql, usuario) 
        result = cursor.fetchone()
    
        return result
