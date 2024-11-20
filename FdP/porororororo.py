# En una escuela de alta especialización en informática se evalúa a postulantes. 
# A c/u se les toma 4 exámenes, cada exámen tiene una puntuación de 0 a 100 ptos,
# para calcular el promedio se desconta la nota más alta y la nota más baja
# considerando sólo las 2 notas intermedias. Escribir un algorítmo modular
# que calcule el promedio de un postulante.

import math

class Vec2:
    """Un vector en el epacio 2D
    """
    def __init__(self, coord_x: float, coord_y: float):
        self.x = coord_x
        self.y = coord_y

    def abs(self):
        abs_vec = (self.x ** 2 + self.y ** 2) ** 0.5
        return abs_vec
    
    def angle(self):
        if self.x >= 0:
            if self.y == 0:
                angle = math.radians(0)
            elif self.y > 0:
                angle = math.atan(self.y / self.x)
            else:
                angle  = 2*math.pi + math.atan(self.y / self.x)
        else:
            if self.y == 0:
                angle = -math.pi
            elif self.y > 0:
                angle = math.pi + math.atan(self.y / self.x)
        return angle

    def __str__(self):
        return f"({self.x}, {self.y})"

vectorPrueba = Vec2(12, 42)

def main():
    print(vectorPrueba)

if __name__ == "__main__":
    main()