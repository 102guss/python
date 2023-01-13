edad = input("ingresa tu edad: ")
nuevaEdad = int(edad)
if nuevaEdad >= 18:
    print("tu edad es: ",nuevaEdad)
    print("Eres meyor de edad, puedes tramitar  tu INE")
elif nuevaEdad <= 0:
    print("la edad no es válida")
else:
     print("aún no puedes tramitar tu INE")

