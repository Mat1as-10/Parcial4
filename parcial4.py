Reserva_zapatillas = {}
Stock_zapatillas = 20
def reservar_zapatillas():
    while True:
        nombre = input("Ingrese su nombre: ").upper
        if nombre not in Reserva_zapatillas:
            break
        else:
            print("Nombre de usuario duplicado.")
            continue
    while True:
        codigo_secreto = input("Ingresa el codigo secreto: ")
        if codigo_secreto == "EstoyEnListaDeReserva":
            Reserva_zapatillas[nombre] = 1 
            print("reserva registrada exitosamente")
            break
        else:
            print ("Codigo secreto invalido.")
            continue


def buscar_reserva(Reserva_zapatillas):
    while True:
        buscador = input("Ingrese el nombre de la reserva: ")
        if buscador not in Reserva_zapatillas:
            print ("Reserva no encontrada.")
            continue
        else:
            print ("reserva encontrada.")
            print(Reserva_zapatillas)
            break

def cancelar_reserva(Reserva_zapatillas):
    while True:
        buscador = input("Ingrese nombre para eliminar reserva: ")
        if buscador not in Reserva_zapatillas:
            print ("Reserva no encontrada.")
            continue
        else:
            del Reserva_zapatillas[buscador]
            print("Reserva eliminada.")
            break

while True:
    print("TOTEM AUTOATENCIÓN RESERVA STRIKE")
    print("[1] Reservar zapatillas")
    print("[2] Buscar zapatillas reservadas")
    print("[3] Cancelar reserva de zapatillas")
    print("[4] Salir")
    
    eleccion = input("Ingrese una opcion (1 - 4): ")
    if eleccion == "1":
        reservar_zapatillas()
    elif eleccion == "2":
        buscar_reserva()
    elif eleccion == "3":
        cancelar_reserva()
    elif eleccion == "4":
        print ("Cierre de programa...")
        break


