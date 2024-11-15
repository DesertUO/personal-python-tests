# Dado un número de 4 cifras,
# escribir un programa que determine el número de dígitos pares.

# Leer los datos (un número de 4 cifras)
Nro = int(input("Ingrese un número de 4 cifras: "))
# Descomponer el número
unidad = Nro % 10
decena = (Nro // 10) % 10
centena = (Nro // 100) % 10
millar = Nro // 1000
# Determinar el número de cifras pares
cifrasPares = ((unidad + 1) % 2) + ((decena + 1) % 2) + ((centena + 1) % 2) + ((millar + 1) % 2)
# Mostrar los resultados (el número de cifras pares)
print("El número de cifras pares del número es de", cifrasPares)
