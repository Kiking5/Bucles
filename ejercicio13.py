"""Escribir un programa que muestre el eco de todo lo que el usuario 
introduzca hasta que el usuario escriba “salir” que terminará."""

while True:
    frase = input("Introduce cualquier cosa: ")
    if frase == "salir":
        break
    print((f"Usted Ingreso: {frase}\n")*100)