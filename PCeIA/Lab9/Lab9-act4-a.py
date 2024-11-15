# Calcular el área de un trapecio

# Leer los datos (base mayor, base menor y la altura del trapecio)
baseMayor = int(input("Ingrese la base mayor: "))
baseMenor = int(input("Ingrese la base menor: "))
altura = int(input("Ingrese la altura: "))
# Calcular el área del trapecio
Area = ((baseMayor + baseMenor) * (altura)) / 2
# Mostrar los resultados (el área del trapecio)
print("El área del trapecio es:", Area)
