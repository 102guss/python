x = input("Introduce el numero de renglones del marco: ")
numero = int(x)
rango = range(numero)

for i in rango:
    print(" *",end = "")

for j in range(numero-2):
    print("  ")#espacio en blanco
    print(" *",end="")
    for k in range(numero-2):
        print("  ",end="")#dos espacios en blanco
    print(" *",end="")
print("  ")#espacio en blanco

for  m in rango:
    print(" *",end="")
