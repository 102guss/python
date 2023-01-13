#practicado la tabla del ciclo for básico


# x=1
# numeros=range(1,11)
# for i in numeros:
#     resultad= x*i
#     print(x,"X",i,"=",resultad)



# x=1
# array=[1,2,3]
# for j in array:
#     numeros=range(1,11)
#     for i in numeros:
#         resultad= x*i
#         print(x,"X",i,"=",resultad)
#     x=x+1
#     print("\n")


#el usuari ingresará un numeroo y de ahi en adelant empezaran las tablas de multilicar hasta el 10
#ste es e for mejorado de las tablas de multipicar compusta
x=input("Ingrsa un numero: ")
numero=int(x)
print()
arregl=range(numero,11)
for j in arregl:
     for i in range(1,11):
         result=numero*i
         print(numero,"X",i,"=",result)
     numero+=1
     print()


