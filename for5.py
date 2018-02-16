#codiing: utf8
num = int(input("Cuántos valores vas a introducir"))

if numero <= 0:
    print("Imposible. Intentalo otra vez")
else:
    cont = 0
    for i in range(1, numero + 1):
        valor = int(input("Escriba el numero" + str(i) + ":"))
        if valor < 0:
            cont = cont + 1
    if cont == 0:
        print("No has escrito ningún numero negativo")
    if cont == 1:
        print("Has escrito 1 número negativo")
    else:
        print"Has escrito", cont "números negativos")
