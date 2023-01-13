x = input("Introduce el numero de renglones del marco: ")
numero = int(x)
rango = range(numero)

for j in  rango:
    for i in rango:
        if (j==0) or (j==numero-1) or (i==0) or (i==numero-1):
         print(" *",end="")
        else:
         print("  ",end="")
    print("")#salto de linea
        

