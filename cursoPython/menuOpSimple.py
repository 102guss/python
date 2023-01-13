
print("...........MENÚ CALCULADORA................")
print()
a=input("dijita un número: ")
num1=int(a)
b=input("dijita otro numero: ")
num2=int(b)
print()
print("1-suma")
print("2-resta")
print("3-multiplicació")
print("4-division")
print()
op=input("digite una opcion: ")

if op == "1":
    print("la suma es: ",num1+num2)
elif op =="2":
    print("la resta es: ", num1-num2)
elif op=="3":
    print("la multiplicacion es: ",num1*num2)
elif op=="4":
    if num2==0:
        print("la division no existe en lo numeros reales")
    else:
     print("la division es: ",num1/num2)
else:
    print("opcion no valida")