#utilizando do while: segunda forma
while True:
    x = input("ingresa tu edad:")
    edad = int(x)
    if edad <= 0:
         print("Rango Incorrecto, intente de nuevo")
    else:
        break
        
        
if edad > 0 and edad <18:
    print("Eres menor de edad, no puedes tramitar tu INE")  
else:
    print("Felicidades, puedes tramitar tu ine, eres mayor de dad ")
