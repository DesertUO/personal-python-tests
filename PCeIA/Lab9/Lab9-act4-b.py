# Calcular la distancia entre 2 puntos

# Leer los datos (2 puntos)
x1 = float(input("Ingrese la coordenada x del punto 1: "))
y1 = float(input("Ingrese la coordenada x del punto 1: "))
x2 = float(input("Ingrese la coordenada y del punto 2: "))
y2 = float(input("Ingrese la coordenada y del punto 2: "))
# Calcular la distancia la distancia entre los 2 puntos
Dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
# Mostrar los resultados (la distancia entre los 2 puntos)
print("La distancia es:", Dist)
