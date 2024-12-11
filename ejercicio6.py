"""Escribir un programa que pida al usuario un número entero y muestre por 
pantalla un triángulo rectángulo como el de más abajo, de altura el número 
introducido."""

numero = int(input("Ingrese la altura del triángulo: "))
for fila in range(numero):
    for columna in range(fila+1):
        print("*", end="")
    print("")