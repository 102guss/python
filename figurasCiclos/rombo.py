x = input("Introduce el numero de renglones del rombo: ")
numero = int(x)
rango = range(numero+1)
contador=0

for i in rango:
    for k in reversed(rango):
        if k>0:
            print("-",end="")
    for m in rango:
        if m<i:
           print(" *",end="")
    print("-",end="")
    print()#salto de linea



