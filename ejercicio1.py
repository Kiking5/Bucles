"""Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces."""

palabra = input("Ingrese una palabra: ")
contador = 0
while contador < 10:
    print(palabra)
    contador += 1
