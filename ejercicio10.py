"""Escribir un programa que pida al usuario un número entero positivo 
mayor que 2 y muestre por pantalla si es un número primo o no."""

numero = int(input("Ingrese un numero mayor que dos (2), para verificar si es primo: "))

for i in range(2, numero):
    if numero % i == 0:
        print(f"{numero} no es primo")
        break
else:
    print(f"{numero} es primo")