import sys
import os


def menu(menu):
    print(" ")
    print("-------------------------------------------")
    print("          Menu Principal")
    print("-------------------------------------------")
    print("1. Reservaciones")
    print("2. Pedidos")
    print("3. Tienda")
    print("4. Facturación")
    print("5. Salir")
    print(" ")
    eleccion = int(input("Digite la opción: "))
    while (eleccion != 6):
        if eleccion == 1:
            reservaciones(menu)
            break
        elif eleccion == 2:
            pedidos()
            break
        elif eleccion == 3:
            tienda()
            break
        elif eleccion == 4:
            facturacion()

        else:
            eleccion == 4
            if input("Seguro (s/n): ") == "s":
                sys.exit()






def reservaciones (precio):
    print(" ")
    print("Mesas disponibles acontinuación: ↓  ↓  ↓")
    mesas = [7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
    precio = 0
    print(mesas)
    print(" ")
    espacios= int(input("Indique la cantidad de mesas que desea ocupar: "))
    for i in range(espacios):
        mesas.remove(int(input("Indique los números según la cantidad de personas: ")))
        print(" ")
    zona = input("Escriba 'normal' para zona común y 'VIP' para zona mejorada: ")
    if zona == "normal":
        precio += 5000
    else:
        precio += 7000
    print(" ")
    print("Reservación Realizada: ")
    print(mesas)
    print(" ")
    print("Precio:", precio)
    menu(precio)




from main import reservaciones
precio = 0
def facturacion(precio):
    print(reservaciones(precio))










def pedidos():
    platofuerte=[[0,3,4],[1,6,8],[2,4,7]]
    liquido=[[3,5],[0,2],[1,4]]
    postrescom=[[2,3],[0,5],[1,4]]
    precio=0

    while True:
        seccion = input("Escriba principales, bebidas o postres según corresponda:")
        if seccion == "principales":
            principales = open("principales.txt", 'r', encoding="utf-8")
            leerpr = principales.read()
            print(leerpr)
            ing=input("Digite 'si' si desea observar los ingredientes de un platillo, digite no para continuar:")
            if ing=="si":
                numeroing = int(input("Inserte numero de plato"))
                ingredientespr = open("ingredientespr.txt", 'r', encoding="utf-8")
                lecting = ingredientespr.readlines()
                print(lecting[numeroing])
            ped= input("Digite 'si' si desea pedir, digite 'no' si desea seguir observando:")
            if ped=="si":
                numeroplat=int(input("Inserte numero de plato principal"))
                principales = open("principales.txt", 'r', encoding="utf-8")
                plato= principales.readlines()
                print(plato[numeroplat])
                italia=platofuerte[0]
                usa=platofuerte[1]
                francia=platofuerte[2]
                if numeroplat in italia:
                    precio2=20000
                    precio+=precio2
                elif numeroplat in usa:
                    precio2=10000
                    precio+=precio2
                elif numeroplat in francia:
                    precio2=30000
                    precio+=precio2
                with open("factura.txt", "a", encoding="utf-8") as file:
                    file.write("Precio del platillo: " + str(precio2) + '\n')
                file.close()
                print(precio)
                cont= input("Digite si si desea continuar con el pedido, digite no si desea terminar:")
                if cont == "si":
                    pass
                else:
                    with open("factura.txt", "a", encoding="utf-8") as file:
                        file.write("Precio total" + str(precio) + '\n')
                    factura = open("factura.txt", 'r', encoding="utf-8")
                    contenido = factura.read()
                    print(contenido)
                    factura.close()
                    break
            if ped =="no":
                pass
        elif seccion == "bebidas":
            bebidas = open("bebidas.txt", 'r', encoding="utf-8")
            leerb = bebidas.read()
            print(leerb)
            ing = input("Digite 'si' si desea observar los ingredientes de una bebida, digite no para continuar:")
            if ing == "si":
                numeroingb = int(input("Inserte numero de bebida:"))
                ingredientesb = open("ingredientesb.txt", 'r', encoding="utf-8")
                lectingb = ingredientesb.readlines()
                print(lectingb[numeroingb])
            ped = input("Digite 'si' si desea pedir, digite 'no' si desea seguir observando:")
            if ped == "si":
                numerob = int(input("Inserte numero de bebida"))
                bebidas = open("bebidas.txt", 'r', encoding="utf-8")
                bebida = bebidas.readlines()
                print(bebida[numerob])
                italia = liquido[0]
                usa = liquido[1]
                francia = liquido[2]
                if numerob in italia:
                    precio3=9000
                    precio += precio3
                elif numerob in usa:
                    precio3 = 3000
                    precio +=precio3
                elif numerob in francia:
                    precio3 = 6000
                    precio += precio3
                with open("factura.txt", "a", encoding="utf-8") as file:
                    file.write("Precio de la bebida: " + str(precio3) + '\n')
                    file.close()
                print(precio)
                cont= input("Digite si si desea continuar con el pedido, digite no si desea terminar:")
                if cont == "si":
                    pass
                else:
                    with open("factura.txt", "a", encoding="utf-8") as file:
                        file.write("Precio total: " + str(precio) + '\n')
                    factura = open("factura.txt", 'r', encoding="utf-8")
                    contenido = factura.read()
                    print(contenido)
                    factura.close()
                    break
            if ped == "no":
                pass
        elif seccion== "postres":
                postres = open("postres.txt", 'r', encoding="utf-8")
                leerpo = postres.read()
                print(leerpo)
                ing = input("Digite 'si' si desea observar los ingredientes de un postre, digite no para continuar:")
                if ing == "si":
                    numeroingpo = int(input("Inserte numero de postre:"))
                    ingredientespo = open("ingredientespo.txt", 'r', encoding="utf-8")
                    lectingpo = ingredientespo.readlines()
                    print(lectingpo[numeroingpo])
                ped = input("Digite 'si' si desea pedir, digite 'no' si desea seguir observando:")
                if ped == "si":
                    numeropo = int(input("Inserte numero de postre:"))
                    postres = open("postres.txt", 'r', encoding="utf-8")
                    postre = postres.readlines()
                    print(postre[numeropo])
                    italia = postrescom[0]
                    usa = postrescom[1]
                    francia = postrescom[2]
                    if numeropo in italia:
                        precio4= 10000
                        precio += precio4
                    elif numeropo in usa:
                        precio4 = 15000
                        precio += precio4
                    elif numeropo in francia:
                        precio4 = 5000
                        precio += precio4
                    with open("factura.txt", "a", encoding="utf-8") as file:
                        file.write("Precio del postre: " + str(precio4) + '\n')
                        file.close()
                    print(precio)
                    cont = input("Digite si si desea continuar con el pedido, digite no si desea terminar:")
                    if cont == "si":
                        pass
                    else:
                        with open("factura.txt", "a", encoding="utf-8") as file:
                            file.write("Precio total: " + str(precio) + '\n')
                        factura= open("factura.txt",'r', encoding="utf-8")
                        contenido= factura.read()
                        print(contenido)
                        factura.close()
                        break
                if ped == "no":
                    pass
                    menu()









import sys
def tienda():
 nombres = []
 precios = []
 cantidades_vendidas = []

 while True:
    print("""
  =========================


  =========================
  """)
    eleccion = input("""
1 - Introducir un artículo nuevo
2 - Hacer una venta
3 - Mostrar información
4 - Borrar un artículo
5 - Borrar todos los artículos
6 - Salir
Seleccione: """)
    if eleccion == "1":
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio del producto: "))
        cantidad_vendida = 0.0
        nombres.append(nombre)
        precios.append(precio)
        cantidades_vendidas.append(cantidad_vendida)
    elif eleccion == "2":
        nombre_articulo = input("Nombre del artículo que se vende: ")
        if nombre_articulo in nombres:
            cantidad = float(input("Cantidad vendida: "))
            indice = nombres.index(nombre_articulo)
            precio = precios[indice]
            cantidades_vendidas[indice] += cantidad
            print(
                f"Se vende(n) {cantidad} {nombre_articulo}. Total: {cantidad * precio}")
        else:
            print("El artículo no existe")
    elif eleccion == "3":
        if len(nombres) <= 0:
            print("No hay artículos")
            continue
        # Los nombres de artículos
        articulo_mas_vendido = nombres[0]
        articulo_menos_vendido = nombres[0]
        articulo_con_mas_ingresos = nombres[0]
        articulo_con_menos_ingresos = nombres[0]
        # Pero también necesitamos el conteo. Simplemente los inicializamos en un elemento del arreglo
        mas_vendido = cantidades_vendidas[0]
        menos_vendido = cantidades_vendidas[0]
        con_mas_ingresos = cantidades_vendidas[0] * precios[0]
        con_menos_ingresos = cantidades_vendidas[0] * precios[0]
        print("+--------------------+----------+----------+----------+")
        print("|NOMBRE              |CANT.     |PRECIO    |IMPORTE   |")
        print("+--------------------+----------+----------+----------+")
        indice = 0
        total = 0
        while indice < len(nombres):
            nombre = nombres[indice]
            precio = precios[indice]
            cantidad_vendida = cantidades_vendidas[indice]
            importe = precio * cantidad_vendida
            print("|{:<20}|{:>10.2f}|{:>10.2f}|{:>10.2f}|".format(
                nombre, cantidad_vendida, precio, importe))
            print("+--------------------+----------+----------+----------+")
            if cantidad_vendida > mas_vendido:
                mas_vendido = cantidad_vendida
                articulo_mas_vendido = nombre
            if cantidad_vendida < menos_vendido:
                menos_vendido = cantidad_vendida
                articulo_menos_vendido = nombre
            if importe > con_mas_ingresos:
                con_mas_ingresos = importe
                articulo_con_mas_ingresos = nombre
            if importe < con_menos_ingresos:
                con_menos_ingresos = importe
                articulo_con_menos_ingresos = nombre
            total += importe
            indice += 1

        print(
            "|--------------------|----------|TOTAL:    |{:>10.2f}|".format(total))
        print("+--------------------+----------+----------+----------+")
        print(
            f"Artículo más vendido: {articulo_mas_vendido}, con {mas_vendido} unidades")
        print(
            f"Artículo menos vendido: {articulo_menos_vendido}, con {menos_vendido} unidades")
        print(
            f"Artículo con más ingresos: {articulo_con_mas_ingresos}, con {con_mas_ingresos} euros")
        print(
            f"Artículo con menos ingresos: {articulo_con_menos_ingresos}, con {con_menos_ingresos} euros")
    elif eleccion == "4":
        nombre_articulo = input("Nombre del artículo que se elimina: ")
        if nombre_articulo in nombres:
            indice = nombres.index(nombre_articulo)
            del nombres[indice]
            del precios[indice]
            del cantidades_vendidas[indice]
            print(f"Se elimina {nombre_articulo}")
        else:
            print("El artículo no existe")

    elif eleccion == "5":
        if input("Seguro (s/n): ") == "s":
            nombres = []
            precios = []
            cantidades_vendidas = []

    elif eleccion == "6":
        if input("Seguro (s/n): ") == "s":
            sys.exit()
 menu()
menu(precio)

