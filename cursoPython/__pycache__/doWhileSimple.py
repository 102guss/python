# n="no"

# while True:

#     x=input("dijita un numero: ")
#     numero=int(x)
#     s=input("desea seguir continuando? si/no: ")
#     if s==n:
#         print("gracias por su participar FIN")
#         break
#cualquier otro caso que no sea la cadena "no" te lo va a agarrar, seguirá cn el ciclo
#........................................................
#aumentando la dificultad
n="no"
s="si"

while True:

    x=input("dijita un numero: ")
    numero=int(x)
    y=input("desea seguir continuando? si/no: ")
    if y==s:
        continue
    elif y==n:
        print("Gracias por participar FIN")
        break
    else:
        print("opcion no válida, vuelva a intentar")
        