x = input("Introduce el numero de renglones del la semi Pirámide: ")
numero = int(x)

rango = range(numero)
print("el rango es: ",type(numero))
for j in rango:
    for i in rango:
        if i<=j:
            print("*",end="")
        else:
            print(" ",end="")
    print()#salto de linea
    #semi piramide terminada
