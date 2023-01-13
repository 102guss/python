
#utilizando ciclo while normal
contador=1
#edad=0
x = input("ingresa tu edad:")
# print("direccion de la variable x",id(x))
edad = int(x)
# print("direccion de la variable edad: ",id(edad))

if edad <=0:
    print("edad no válida, intenta de nuevo")
   
    while edad<=0 and contador<=2:
        #print("contador vale: ",contador)
        x = input("ingresa tu edad:")
        edad = int(x)
        # print("segunda direccion de la variable x, ",id(x))
        # print("segunda direccion de la variable edad, ",id(edad))
        if edad <=0:
            if contador==2:
                print("se te acabaron los intentos")
            else:
                print("Edad incorrecta, vuelve a intentarlo")
                
            
        elif edad>=18:
            print("Ya puedes tramitar tu INE")
        else:
            print("No puedes tramitar tu INE")
        contador=contador+1

elif edad>=18:
    print("Ya puedes tramitar tu INE")
else:
    print("No puedes tramitar tu INE")
#coom ver la direcion de memoria de una variable?
