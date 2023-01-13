#pograma qie imprime la tabla de multiplicar del uno hasta el  3


contador1=1
numerosTabla2=range(1,4)
for j in numerosTabla2:
    contador1=1
    numerosTabla=range(1,11)
    for i in numerosTabla:
        resultado=contador1*i
        print(contador1,"X",i,"=",resultado)
    contador1=contador1+1
    print("\n")

