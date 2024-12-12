"""Escribir un programa que pida al usuario una palabra y luego muestre 
por pantalla una a una las letras de la palabra introducida empezando por 
la última."""

frase = input("Ingrese una fras cualquiera: ")
letra = input("Ingrese una letra: ")

contador = 0
for i in frase:
    if i == letra:
        contador += 1
print(f"La letra {letra} aparece {contador} veces en la frase: '{frase}.'")