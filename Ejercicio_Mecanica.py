servicios = {
    "frenos": 15000,
    "engrasado": 10000,
    "lavado": 8000,
    "pulido": 12000,
    "especial": 40000
}

ubicaciones = [
    "Concepción",
    "Puente Alto",
    "Muelle Barón - Valdivia",
    "Muelle Vergara - Viña del Mar"
]

usuarios = []

def mostrar_menu():
    print("\n*** MENÚ PRINCIPAL - GIRO ROCK AUTOSERVICIO ***")
    print("[1] Ingresar usuario y seleccionar servicios")
    print("[2] Mostrar ubicaciones")
    print("[3] Salir del programa")

def ingresar_usuario():
    print("\n--- INGRESO DE USUARIO ---")

    nombre = input("Ingrese su nombre: ")
    id_usuario = input("Ingrese su número de ID: ")

   
    print("\nServicios disponibles:")
    for servicio in servicios:
        print(f"- {servicio.capitalize()} --> ${servicios[servicio]}")

    while True:
        servicio_elegido = input("\nIngrese el servicio que desea contratar (o escriba 'especial'): ").lower()
        
        if servicio_elegido == "especial":
            total = servicios["especial"]
            detalle = list(servicios.keys())
            detalle.remove("especial")
            break
        elif servicio_elegido in servicios:
            total = servicios[servicio_elegido]
            detalle = [servicio_elegido]
            break
        else:
            print("Servicio no válido. Intente nuevamente.")

 
    usuario = {
        "nombre": nombre,
        "id": id_usuario,
        "servicios": detalle,
        "total": total
    }
    usuarios.append(usuario)
    print(f"\n¡Compra registrada con éxito para {nombre}!")
    print(f"Servicios contratados: {', '.join(detalle)}")
    print(f"Total a pagar: ${total}")


def mostrar_ubicaciones():
    print("\n--- UBICACIONES DISPONIBLES ---")
    for ubicacion in ubicaciones:
        print(f"- {ubicacion}")


def menu_principal():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            ingresar_usuario()
        elif opcion == "2":
            mostrar_ubicaciones()
        elif opcion == "3":
            print("¡Gracias por usar Giro Rock Autoservicio!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


menu_principal()