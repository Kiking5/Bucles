"""Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla la cuenta atrás desde ese número hasta cero 
separados por comas."""

numero = int(input("Ingrese un numero entero que sea positivo: "))
while numero >= 0:
    print(numero, end="")
    if numero > 0:
        print(", ", end="")
    numero -= 1
