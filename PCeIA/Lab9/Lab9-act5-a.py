# Dado un numero de 3 cifras, escribir un programa que determine el número de dígitos impares.

# Leer los datos (un número de 3 cifras)
Nro = int(input("Ingrese un número de 3 cifras: "))
# Descomponer el número
Unidad = Nro % 10
Decena = (Nro // 10) % 10
Centena = Nro // 100
# Calcular el número de cifras impares
digitosImpares = (Unidad % 2) + (Decena % 2) + (Centena % 2)
# Mostrar los resultados (el número de cifras impares)
print("El número de cifras impares es:", digitosImpares)
