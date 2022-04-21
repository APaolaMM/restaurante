def pedidos():
    platofuerte=[[0,3,4],[1,6,8],[2,4,7]]
    liquido=[[3,5],[0,2],[1,4]]
    postrescom=[[2,3],[0,5],[1,4]]
    precio=0
    while True:
        seccion = input("Escriba principales, bebidas o postres según corresponda")
        if seccion== "principales":
            principales = open("principales.txt", 'r', encoding="utf-8")
            leerpr = principales.read()
            print(leerpr)
            ing=input("Digite 'si' si desea observar los ingredientes de un platillo, digite no para continuar")
            if ing=="si":
                numeroing = int(input("Inserte numero de plato"))
                ingredientespr = open("ingredientespr.txt", 'r', encoding="utf-8")
                lecting = ingredientespr.readlines()
                print(lecting[numeroing])
            ped= input("Digite 'si' si desea pedir, digite 'no' si desea seguir observando")
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
                cont= input("Digite si si desea continuar con el pedido, digite no si desea terminar")
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
            if ped=="no":
                pass
        elif seccion == "bebidas":
            bebidas = open("bebidas.txt", 'r', encoding="utf-8")
            leerb = bebidas.read()
            print(leerb)
            ing = input("Digite 'si' si desea observar los ingredientes de una bebida, digite no para continuar")
            if ing == "si":
                numeroingb = int(input("Inserte numero de bebida"))
                ingredientesb = open("ingredientesb.txt", 'r', encoding="utf-8")
                lectingb = ingredientesb.readlines()
                print(lectingb[numeroingb])
            ped = input("Digite 'si' si desea pedir, digite 'no' si desea seguir observando")
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
                cont= input("Digite si si desea continuar con el pedido, digite no si desea terminar")
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
                ing = input("Digite 'si' si desea observar los ingredientes de un postre, digite no para continuar")
                if ing == "si":
                    numeroingpo = int(input("Inserte numero de postre"))
                    ingredientespo = open("ingredientespo.txt", 'r', encoding="utf-8")
                    lectingpo = ingredientespo.readlines()
                    print(lectingpo[numeroingpo])
                ped = input("Digite 'si' si desea pedir, digite 'no' si desea seguir observando")
                if ped == "si":
                    numeropo = int(input("Inserte numero de postre"))
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
                    cont = input("Digite si si desea continuar con el pedido, digite no si desea terminar")
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
pedidos()