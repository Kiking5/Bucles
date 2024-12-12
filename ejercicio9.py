"""Escribir un programa que almacene la cadena de caracteres contraseña en una 
variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña 
correcta."""

clave = "contraseña"
password =""
while password != clave:
    password = input("Introduce la contraseña: ")
print("Contraseña correcta")