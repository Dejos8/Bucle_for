#coding:utf8
num = int(input("Cuántos valores vas a introducir?"))
if num < 1:
    print("Imposible.Intentalo otra vez")
else:
    pares = 0
    for i in range(1, num + 1):
        numero = int(input("Escriba el valor + str(i) + ":"))
        if numero % 2 == 0:
            pares += 1
    print "Ha escrito str (pares) numeros pares y" str(num - pares) "números impares")
 
