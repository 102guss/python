#utilizando do while: primera forma
while True:
    x = input("ingresa tu edad:")
    edad = int(x)
    if edad > 0:
        break
    else:
         print("Rango Incorrecto, intente de nuevo")
if edad > 0 and edad <18:
    print("Eres menor de edad, no puedes tramitar tu INE")  
else:
    print("Felicidades, puedes tramitar tu ine, eres mayor de dad ")
