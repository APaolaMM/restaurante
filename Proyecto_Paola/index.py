def reservaciones ():
    mesas = [7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
    precio = 0
    print(mesas)
    espacios= int(input("Indique la cantidad de mesas que desea ocupar"))
    for i in range(espacios):
        mesas.remove(int(input("Indique los números según la cantidad de personas")))
        print(mesas)
    zona= input("Escriba 'normal' para zona común y 'VIP' para zona mejorada")
    if zona=="normal":
        precio+= 5000
    else:
        precio+= 7000
    print(precio)
reservaciones()