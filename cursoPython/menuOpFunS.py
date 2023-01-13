def suma(n1,n2):
    return n1+n2

def resta(n1,n2):
    return n1-n2

def multi(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

# print("...........MENÚ CALCULADORA................")
# print()
# a=input("dijita un número: ")
# num1=int(a)
# b=input("dijita otro numero: ")

# num2=int(b)
# print()
# print("1-suma")
# print("2-resta")
# print("3-multiplicación")
# print("4-division")
# print()
# op=input("digite una opcion: ")
# if op == "1":
#     print("la suma es: ",suma(num1, num2))
# elif op =="2":
#     print("la resta es: ", resta(num1, num2))
# elif op=="3":
#     print("la multiplicacion es: ",multi(num1, num2))
# elif op=="4":
#     if num2==0:
#         print("la division no existe en lo numeros reales")
#     else:
#      print("la division es: ",div(num1, num2))
# else:
#     print("opcion no valida")

    #lo siguiente es implementarlo con un do while
s="si"
n="no"

while True:

    print("\n...........MENÚ CALCULADORA................")
    print()
    a=input("dijita un número: ")
    num1=int(a)
    b=input("dijita otro numero: ")
    num2=int(b)
    print()
    print("1-suma")
    print("2-resta")
    print("3-multiplicación")
    print("4-division")
    print()
    op=input("digite una opcion: ")
    if op == "1":
        print("la suma es: ",suma(num1, num2))
        x=input("\nquieres seguir haciendo operaciones?: ")
        if x==s:
            continue
        else:
            break  #nota: para las demás opciones tambiien puedo poner un "break" o un "continue"
    elif op =="2":
        print("la resta es: ", resta(num1, num2))
    elif op=="3":
        print("la multiplicacion es: ",multi(num1, num2))
    elif op=="4":
        if num2==0:
            print("la division no existe en lo numeros reales")
        else:
            print("la division es: ",div(num1, num2))
    else:
        print("opcion no valida")
        break
print("\nFIN DEL PROGRAMA")
