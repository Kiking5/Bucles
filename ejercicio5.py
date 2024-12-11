"""Escribir un programa que pregunte al usuario una cantidad a invertir, el interés 
anual y el número de años, y muestre por pantalla el capital obtenido en la inversión 
cada año que dura la inversión."""

inversion = int(input("Ingrese la cantidad a invertir: "))
interes = float(input("Ingrese el interés anual: "))
anios = int(input("Ingrese la cantidad de años: "))

for anio in range(anios):
    inversion *= 1 +interes/100
    print(f"Su capital despued de {anio+1} años es de: {round(inversion, 2)}")