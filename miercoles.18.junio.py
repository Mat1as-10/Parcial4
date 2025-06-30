"""Haga un programa que permita generar un menú, de gestionar de entradas para el concierto de gihub con movimientos originales, 
con sus diferentes shows. El menú principal debe permitir mostrar 4 opciones 
MENU PRINCIPAL:
1: Venta de entradas 
2: Cambio de show 
3: Mostrar stock de funciones
4: Salir del programa 
Todas las opciones del menú deben estar implementadas mediante funciones separadas del codígo principal (MAIN)
Al ingresar a la opción numero 1 puedo comprar entradas, se debe permitir ingresar 
NOMBRE 
SELECCIONAR SHOW
Por separado.
Para que la compra sea exitosa se debe cumplir con los siguientes requerimientos:
A) el nombre del comprador no debe estar repetido
B) la selección del show debe permitir seleccionar entradas para una de las dos funciones.
Funcion numero 1: Movimientos originales con la tripulación.
Funcion numero 2: Movimientos originales con sonrisa.
C) debe haber un máximo  de 50 entradas en caso de cumplir co todas las condiciones, la entrada se registrara como exitosa 
al ingresar la opción numero 2 cambio de show, el menú debe permitir cambiar la entrada al show 1 o al show 2 
Opciones numero 3 mostrar total de entradas disponibles para cada una de las funciones 
Opciones numero 4 salir del sistema 
si el usuario comete un error y decida ingresar cualquier opción que no es la permitida debemos mostrar un mensaje 
que diga ingresa solo opciones permitidas """
# Diccionario para llevar el stock
stock = {
    "show1": 50,
    "show2": 50
}

# Lista para guardar los compradores y sus funciones
compradores = []

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1: Venta de entradas")
    print("2: Cambio de show")
    print("3: Mostrar stock de funciones")
    print("4: Salir del programa")

def venta_entradas():
    nombre = input("Ingrese su nombre: ").strip()
    
    # Verificar nombre repetido
    if any(comp["nombre"].lower() == nombre.lower() for comp in compradores):
        print("❌ Este nombre ya ha comprado una entrada.")
        return

    print("\nSeleccione show:")
    print("1: Movimientos originales con la tripulación")
    print("2: Movimientos originales con sonrisa")
    opcion = input("Ingrese 1 o 2: ").strip()

    if opcion == "1" and stock["show1"] > 0:
        compradores.append({"nombre": nombre, "show": "show1"})
        stock["show1"] -= 1
        print("✅ Entrada comprada para el show 1.")
    elif opcion == "2" and stock["show2"] > 0:
        compradores.append({"nombre": nombre, "show": "show2"})
        stock["show2"] -= 1
        print("✅ Entrada comprada para el show 2.")
    else:
        print("❌ Opción inválida o no hay stock disponible.")

def cambio_de_show():
    nombre = input("Ingrese su nombre para cambiar el show: ").strip()
    comprador = next((c for c in compradores if c["nombre"].lower() == nombre.lower()), None)

    if comprador is None:
        print("❌ No se encontró ese nombre.")
        return

    show_actual = comprador["show"]
    nuevo_show = "show2" if show_actual == "show1" else "show1"

    if stock[nuevo_show] <= 0:
        print("❌ No hay entradas disponibles para el otro show.")
        return

    # Hacer el cambio
    comprador["show"] = nuevo_show
    stock[show_actual] += 1
    stock[nuevo_show] -= 1
    print(f"✅ Cambio realizado. Ahora estás inscrito en {nuevo_show}.")

def mostrar_stock():
    print("\n🎟️ Stock disponible:")
    print(f"Show 1 - Movimientos originales con la tripulación: {stock['show1']} entradas")
    print(f"Show 2 - Movimientos originales con sonrisa: {stock['show2']} entradas")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            venta_entradas()
        elif opcion == "2":
            cambio_de_show()
        elif opcion == "3":
            mostrar_stock()
        elif opcion == "4":
            print("👋 Saliendo del sistema. ¡Gracias!")
            break
        else:
            print("❌ Ingresa solo opciones permitidas.")

# Ejecutar programa
if __name__ == "__main__":
    main()