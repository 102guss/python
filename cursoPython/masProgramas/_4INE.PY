#SEGUNDA FORMA UTILIZANDO DO WHILE CON SENTEMCIA DE CONTROL: ELIF
while True:
    x=input("ingresa tu edad: ")
    edad=int(x)
    if edad <= 0: #el "cero" es la clave para poner a prueba al "if" "else"
        print("edad no válida, intenta de nuevo")
    else:
        break
if edad == 1:
    print("apoco tienes un añode nacido? ")
elif edad ==2:
    print("tu edad es dos?")    
elif edad > 2 and edad < 18:
    print("aún no puedes tramitar tu INE")
else:
   print ("Felicidades!, puedes tramitar tu INE")
            


