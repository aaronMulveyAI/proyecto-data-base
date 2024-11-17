from usuarios import acciones

print("""
      Acciones disponibles:
        - registro
        - login
      """)  

haz_el = acciones.Acciones()

action = input("Que quieres hacer: ")

if action == "registro":
    haz_el.registro()
elif action == "login":
    haz_el.login()
    