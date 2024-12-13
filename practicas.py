# bucles inmprime Felicidades, tienes x años hasta llegar a 18

"""edad = 0
while edad < 18:
 edad = edad + 1
 print (f"Felicidades, tienes {edad}")"""

# contrar hacia atrás desde 23

"""numero=10
while numero > 0:
    print(numero)
    numero = numero -1
print("El conteo ha finalizado!")"""

# Bucle infinito hasta que ingrese fin

"""while True:
    linea = input("Ingresa un dato: " )
    if linea == "fin":
        break
    printprint(f"Usted ha ingresado: {linea}")
print("Finalizado!")"""

# terminar iteraciones con continue

"""while True:
    linea = input("Ingresa un dato: ")
    if linea[0] == "#" :
        continue
    if linea == "fin":
        break
    print(f"Usted ha ingresado: {linea}")
print("Finalizado!")"""

# bucle for

"""amigos = ["Juan", "Andres", "John", "Angie"]
for amigo in amigos:
    print(f"Feliz año nuevo {amigo}")
print("Finalizado!")"""

# Contar cantidad de elementos 

contador = 0
for valor in [3, 41, 12, 9, 74, 15]:
    contador = contador + 1
print(f"La cantidad de elemento es de: {contador}")

# suma los valores

total = 0
for valor in [3, 41, 12, 9, 74, 15]:
    total = total + valor
print(f"El total es: {total}")

# encontrar el valor mayor en una lista

mayor= None
print(f"Numero inicial: {mayor}")
for valor in [3, 41, 12, 9, 74, 15]:
    if mayor is None or valor > mayor :
        mayor = valor
    print(f"El numero es {valor}, el mayor ahora es: {mayor}")
print(f"El mayor es: {mayor}")

# encontrar el valor menor en una lista

menor= None
print(f"Numero inicial: {menor}")
for valor in [3, 41, 12, 9, 74, 15]:
    if menor is None or valor < menor :
        menor = valor
    print(f"El numero es {valor}, el menor ahora es: {menor}")
print(f"El menor es: {menor}")

# iterar sobre los indices

frase = ["Cata", "es", "una", "mujer", "muy", "hermosa"]
for i in range(len(frase)):
    print(i+1, frase[i]) # print(i, a[i]) <= es igual a lista con el numero de indice desde cero (0)

# Números primos en un rango determinado

numero = int(input("Ingrese hasta que numero quiere ver los números primos: "))
for i in range(2, numero+1):
    for j in range(2, i):
        if i % j == 0:  # Verifica si n es divisible por x sin dejar residuo (es decir, si x es un factor de n)
            print(i, "Es igual a", j, "*", i//j)  # Si se encuentra un factor, imprime la relación y sale del bucle interno
            break
    else:
        print(i, "Es un número primo")


# recorrer indices

alumnos = {"Pedro":20, "juan":19, "Maria":21, "Marcela":17}
for i in alumnos:
    print(f"Alumno: {i}")

# recorrer clave

for i in alumnos:
    print(f"La edad de {i} es: {alumnos[i]}")
