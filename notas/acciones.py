import notas.nota as modelo

class Acciones:
    
    def crear(self, usuario):
        print(f"Okay {usuario[1]}, vamis a crear una nueva nota...")
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Introduce el contenido de tu nota: ")
        
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()
        
        if guardar[0] >= 1:
            print("Has guardado tu nota")
        else:
            print("Error al guardar nota")
            
    
    def mostrar(self, usuario):
        print(f"Okay {usuario[1]}, vamis a mostar tus notas...")
    
        nota = modelo.Nota(usuario[0], '', '')
        notas = nota.listar()
        print(notas)
        
    def borrar(self, usuario):
        print(f"Okay {usuario[1]}, vamis a borrar tus nota...")

        titulo = input("Introduce el titulo de la nota a borrar: ")
        
        nota = modelo.Nota(usuario[0], titulo, '')
        eliminar = nota.eliminar()
        if eliminar[0] >= 1:
            print("Nota borrada")
        else:
            print("Nota no encontrada")
            
            

            
    
    
    