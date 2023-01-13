x = input("Introduce el numero de renglones del la semi Pirámide: ")
numero = int(x)
rango = range(numero)
for i in rango:
    for j in range( numero-i ):
        print(" ",end="")
    for k  in range(2*(i+1)-1):
        print("*",end="")
    print()#salto de 
#piramide completa terminada

