#utilizando ciclo while normal

x = input("ingresa tu edad:")
edad = int(x)
if edad<=0:
    print("edad no validaaa, intente de nuevo")
while edad <= 0:
    x = input("ingresa tu edad:")
    edad = int(x)
    if edad <=0:
        print("Edad no valida, intente de nuevo")

if edad > 0 and edad < 18:
    print(" no puedes tramitar tu INE. Eres menor de edad")
else:
    print("Felicidades puedes tramitar tu INE. eres mayor de edad")

   
    