import usuarios.usuario as modelo
import notas.acciones as acciones

class Acciones:

    def registro(self):
        print("OK, vamos a registrate en el sistema...")
        nombre = input("Cual es tu nombre: ")
        apellidos = input("Cual es tu apellido: ")
        email = input("Cual es tu email: ")
        password = input("Cual es tu contraseña: ")
        
        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()
        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado correctamente...")
        else:
            print(f"{registro[1].nombre}, no te has podido registrar cambia de email")
        
    def login(self):
        print("Vale, Identificate en el sistema...")
        email = input("Cual es tu email: ")
        password = input("Cual es tu contraseña: ")
        
        usuario = modelo.Usuario('', '', email, password)
        login = usuario.identificar()
        
        if login is not None and email == login[3]:
            print(f"Bienvenido {login[1]}")
            self.proximasAcciones(login)
        else:
            print("Email o contraseña incorrectos")
            
            
    
    def proximasAcciones(self, usuario):
        print("""
              Acciones disponibles:
                - Crear nota (crear)
                - Mostrat notas (mostrar)
                - Eliminar nota (eliminar)
                - Salir (salir)
              """)
        accion = input("Que quieres hacer? ")
        
        haz_el = acciones.Acciones()
        
        if accion == "crear":
            print("Vamos a crear")
            haz_el.crear(usuario)    
            
        elif accion == "mostrar":
            print("Vamos a mostrar")
            haz_el.mostrar(usuario)
            
        elif accion == "eliminar":
            print("Vamos a eliminar")
            haz_el.borrar(usuario)
            
        elif accion == "salir":
            exit()
            
        self.proximasAcciones(usuario)
            
        