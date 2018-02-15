 #coding: utf­8
num1 = int(input("Escriba tu numero entero: "))
num2 = int(input("Escriba tu numero entero mayor o igual que", str(num1), ":"))
if num2 < num1:

   print "Le he pedido un número entero mayor o igual que", num1

else:

     for i in range(num1, num2 + 1):
          if i % 2 == 0:
              print "el numero", i, "es par"

          else:
               print "el numero", i, "es impar"


     
