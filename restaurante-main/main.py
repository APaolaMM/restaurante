import sys
import os

from index import reservaciones,pedidos,tienda,facturacion,calificacion
def menu():
    print(" ")
    print("-------------------------------------------")
    print("          Menu Principal")
    print("-------------------------------------------")
    print("1. Reservaciones")
    print("2. Pedidos")
    print("3. Tienda")
    print("4. Facturación")
    print("5. Calificación")
    print("6. Salir")
    print(" ")
    eleccion = int(input("Digite la opción: "))
    while (eleccion != 7):
        if eleccion == 1:
            reservaciones()
            break
        elif eleccion == 2:
            pedidos()
            break
        elif eleccion == 3:
            tienda()
            break
        elif eleccion == 4:
            facturacion()
        elif eleccion ==5:
            calificacion()
        else:
            eleccion == 6
            if input("Seguro (s/n): ") == "s":
                sys.exit()
menu()

