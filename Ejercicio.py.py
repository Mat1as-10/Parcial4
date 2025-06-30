"""Ejercicio: Gestión de Usuarios en una Aplicación
Enunciado:
Estás desarrollando un pequeño sistema de administración de usuarios para una aplicación. El objetivo es permitir que el usuario pueda:
Ingresar nuevos usuarios.
Buscar usuarios existentes.
Eliminar usuarios del sistema.
Salir del programa.
Cada usuario debe tener:
Un nombre único.
Un sexo que debe ser "M" (masculino) o "F" (femenino).
Una contraseña válida, que cumpla con los siguientes requisitos:
Al menos 8 caracteres.
No debe contener espacios.
Debe contener al menos una letra y un número.
El programa principal debe mostrar un menú con las opciones mencionadas y actuar en consecuencia. 
Usa un diccionario llamado d para almacenar los usuarios.}"""

registro_usuarios = {}

def ingreso_usuario():
    while True:
        nombre = input ("Ingrese su nombre: ")
        if nombre not in registro_usuarios:
            break
        else:
            print ("Nombre de usuario ya ingresado, intente con otro.")
    while True:
        sexo = input ("Ingrese su sexo (M (Masculino) F (Femenino): )").upper()
        if sexo == "M" or sexo == "F":
            break
        else:
            print ("Ingrese su sexo con las iniciales F o M.")
    while True:
        contraseña = input ("Ingrese su contraseña: ")
        if len(contraseña) < 8 or not any(c.isalpha() for c in contraseña) or not any(c.isdigit() for c in contraseña) or " " in contraseña:
            print ("ERROR. La contraseña debe tener almenos 8 y debe tener una letra y un numero")
            continue
        else:
            break
    registro_usuarios[nombre] = {"sexo": sexo, "contraseña": contraseña}

    print ("Ingreso exitoso.")

def buscar_usuario(registro_usuarios):
    nombre = input("Ingrese el nombre del usuario que deseas buscar: ")
    if nombre not in registro_usuarios:
        print ("Usuario no encontrado.")
        return
    else:
        print ("Usuario encontrado")
        print (f"Sexo:{registro_usuarios[nombre]['sexo']}, Contraseña: {registro_usuarios[nombre]['contraseña']} ")

def eliminar_usuario(registro_usuarios):
    nombre = input("Ingrese el nombre del usuario al que quiera eliminar: ")
    if nombre not in registro_usuarios:
        print ("Usuario no encontrado.")
        return
    else:
        print ("Usuario encontrado.")
        del registro_usuarios[nombre]
        print ("Usuario eliminado.")




while True:
    print("[1] Ingresar nuevo usuario")
    print("[2] Buscar usuario existente")
    print("[3] Eliminar usuario del sistema")
    print("[4] Salir del programa")

    eleccion_usuario = input("ingrese una opcion ( 1 - 4 ): ")

    if eleccion_usuario == "1":
        ingreso_usuario()
    elif eleccion_usuario == "2":
        buscar_usuario(registro_usuarios)
    elif eleccion_usuario == "3":
        eliminar_usuario(registro_usuarios)
    elif eleccion_usuario == "4":
        print ("Hasta luego!")
        break



