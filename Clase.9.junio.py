


"""
Realice un programa en python que permita generar un menu de gestion de entradas para el concierto de noche de bruja 
el menu principal debe mostrar 4 opciones 
MENU PRINCIPAL:
[1] COMPRAR ENTRADA 
[2] CONSULTAR COMPRADOR 
[3] CANCELAR COMPRA 
[4] CONTINUAR INGRESANDO VENTAS O SALIR DEL SISTEMA 
todas las opciones del menu deben estar implementadas mediante funciones separadas del codigo principal()
DESCRIPCION DE OPCIONES:
[1] se debe permitir ingresar el nombre del comprador tipo de entrada y codigo de confirmacion por separados
para que la compra sea exitosa se debe cumplir con lo siguiente:
- el nombre del comprador no debe repetirse
- el tipo de entrada debe ser general o VIP, en el caso de GENERAL = 10.000 y VIP = 50.000
- el codigo de confirmacion debe tener un minimo de 6 caracteres que tenga un numero como minimo y que no tenga espacio en blanco
- en el caso de cumplir con todas las condiciones la entrada se registra como exitosa 
[2] El menu debe pedir buscar compradores ya sea por nombre. si el comprador existe deberia mostrar datos asociados:
Nombre de usuario
Tipo de entrada que compro (GENERAL O VIP + Monto)
Codigo de comfirmacion
si no exisre el usuario el mensaje que se mostraria en pantalla seria "comprador no existe"
[3] El menu debe permitir o mostrar una opcion que el permita eliminar un comprador con toda su informacion asociada a dicho comprador
[4] consultar al usuario si desea continuar o desea salir.
"""

compradores = {}

precios = {
    "general": 10000,
    "vip": 50000
}

def comprar_entrada():
    print("\n=== COMPRA DE ENTRADA ===")

    while True:
        nombre = input("Ingrese nombre del comprador: ").strip().lower()
        if nombre == "":
            print("El nombre no puede estar vacío.")
            continue
        if nombre in compradores:
            print("ERROR: Este comprador ya existe. Intente con otro nombre.")
        else:
            break

    while True:
        tipo = input("Ingrese tipo de entrada (General o Vip): ").strip().lower()
        if tipo not in precios:
            print("ERROR: Tipo de entrada no válido. Debe ser General o Vip.")
        else:
            break

    while True:
        codigo = input("Ingrese código de confirmación (mínimo 6 caracteres, sin espacios y al menos un número): ").strip()
        if len(codigo) < 6:
            print("ERROR: El código debe tener mínimo 6 caracteres.")
            continue
        if " " in codigo:
            print("ERROR: El código no debe tener espacios.")
            continue
        if not any(c.isdigit() for c in codigo):
            print("ERROR: El código debe contener al menos un número.")
            continue
        break

    compradores[nombre] = {
        "tipo": tipo,
        "monto": precios[tipo],
        "codigo": codigo
    }
    print(f"Compra exitosa para {nombre.upper()}. Entrada {tipo.upper()} valor ${precios[tipo]}")

def consultar_comprador():
    print("\n=== CONSULTAR COMPRADOR ===")
    nombre = input("Ingrese el nombre del comprador a consultar: ").strip().lower()

    if nombre in compradores:
        datos = compradores[nombre]
        print(f"Comprador: {nombre.upper()}")
        print(f"Tipo de entrada: {datos['tipo'].upper()}")
        print(f"Monto: ${datos['monto']}")
        print(f"Código de confirmación: {datos['codigo']}")
    else:
        print("Comprador no existe.")

def cancelar_compra():
    print("\n=== CANCELAR COMPRA ===")
    nombre = input("Ingrese el nombre del comprador a eliminar: ").strip().lower()

    if nombre in compradores:
        del compradores[nombre]
        print(f"Se ha eliminado exitosamente a {nombre.upper()}.")
    else:
        print("Comprador no existe.")

def continuar_o_salir():
    while True:
        eleccion = input("¿Desea continuar ingresando ventas? (SI/NO): ").strip().lower()
        if eleccion == "si":
            return True
        elif eleccion == "no":
            print("¡Hasta luego!")
            return False
        else:
            print("Ingrese solo SI o NO.")

while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("[1] COMPRAR ENTRADA")
    print("[2] CONSULTAR COMPRADOR")
    print("[3] CANCELAR COMPRA")
    print("[4] CONTINUAR O SALIR DEL SISTEMA")

    opcion = input("Seleccione una opción (1-4): ").strip()

    if opcion == "1":
        comprar_entrada()
    elif opcion == "2":
        consultar_comprador()
    elif opcion == "3":
        cancelar_compra()
    elif opcion == "4":
        if not continuar_o_salir():
            break
    else:
        print("Opción inválida. Ingrese solo números del 1 al 4.")