# En una escuela de alta especialización en informática se evalúa a postulantes. 
# A c/u se les toma 4 exámenes, cada exámen tiene una puntuación de 0 a 100 ptos,
# para calcular el promedio se desconta la nota más alta y la nota más baja
# considerando sólo las 2 notas intermedias. Escribir un algorítmo modular
# que calcule el promedio de un postulante.

# Leer nros enteros
def leerNumeroEntero(texto, vmin, vmax):
    Nro = int(input(texto))
    while (Nro < vmin) or (Nro > vmax):
        print("ERROR Nro fuera de rango...")
        Nro = int(input("Vuelve a ingresar el número: "))
    return Nro

# Leer puntos
def leerPuntos():
    return leerNumeroEntero("Ingrese la nota: ", 0, 100)

# Determinar nro mayor
def mayorNro(nro1, nro2):
    if nro1 >= nro2:
        return nro1
    else:
        return nro2

# Determinar nro menor
def menorNro(nro1, nro2):
    return nro1 + nro2 - mayorNro(nro1, nro2)

# Módulo principal
def main():
    print("Alumno: ")
    Nota1 = leerPuntos()
    Nota2 = leerPuntos()
    Nota3 = leerPuntos()
    Nota4 = leerPuntos()
    
    NotaMayor = mayorNro(mayorNro(Nota1, Nota2), mayorNro(Nota3, Nota4))
    NotaMenor = menorNro(menorNro(Nota1, Nota2), menorNro(Nota3, Nota4))
    
    promedio = (Nota1 + Nota2 + Nota3 + Nota4 - NotaMayor - NotaMenor) / 2
    
    print("El promedio del alumno es: " + str(promedio))

main()