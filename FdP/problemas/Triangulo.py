from libreria_1 import *

# Dado tres puntos en el plano cartesiano. Escriba un programa modular que verifique
# que dichos puntos correspondan a los vértices de un triángulo, luego que calcule el perímetro y el área
# de dicho triángulo

# Verificar si los lados corresponden a un triángulo

# Módulo para verificar los lados dan un triángulo
def EsTriangulo(L1, L2, L3):
    return ((L1 + L2 > L3) and (L2 + L3 > L1) and (L1 + L3 > L2))
# Módulo para calcular el perímetro
def Perimetro(L1, L2, L3):
    return (L1 + L2 + L3)
# Módulo para calcular el área
def Area(L1, L2, L3):
    S = (L1 + L2 + L3 / 2)
    return (S * (S - L1) * (S - L2) * (S - L3)) ** 0.5

# Programa principal

# Leer los vértices del triángulo
vx1, vy1 = LeerPunto("Ingrese las coordenadas del 1er vértice")
vx2, vy2 = LeerPunto("Ingrese las coordenadas del 2do vértice")
vx3, vy3 = LeerPunto("Ingrese las coordenadas del 3er vértice")

# Calcular los lados del triángulo
Lado1 = Distancia(vx1, vy1, vx2, vy2)
Lado2 = Distancia(vx1, vy1, vx3, vy3)
Lado3 = Distancia(vx2, vy2, vx3, vy3)

# Verificación y cálculo
if (EsTriangulo(Lado1, Lado2, Lado3)):
    # Calcular el perímetro
    Perim = Perimetro(Lado1, Lado2, Lado3)
    # Calcular el área
    Area = Area(Lado1, Lado2, Lado3)
    # Mostrar perímetro y área
    print("Perímetro: ", Perim)
    print("Área: ", Area)
else:
    print("Los datos no corresponden a un triángulo")
