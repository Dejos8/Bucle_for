#coding: utf8
valores= int(input("Cuantos valores va a introducir:"))

if valores < 1:
    print("imposible")
else:
    pri = int(input("Escriba un número: "))
    for i in range(valores - 1):
        num= input("Escriba un número más grande que" + str(pri)+ ":")
        if num <= pri:
            print(num, "no es mayor que", pri)

