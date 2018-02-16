#coding:utf8
num1 = int(input("Escriba un número entero: "))
num2 = int(input("Escriba un número entero mayor que" + str(num1) + ":"))

if num2 <= num1:
    print("Le he pedido un número entero mayor o igual que", num1)
else:
    suma = 0
    for i in range(num1, num2 + 1):
        suma = suma + i
    print("La suma desde" + (num1) + "hasta" + str(num2) + "es" + str(suma))

    for i in range(num1, num2):
        print(i)
    print(num2, "=", suma)
