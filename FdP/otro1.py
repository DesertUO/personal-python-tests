# Problema .- Escriba un programa modular
# para calcular el promedio de
# 3 notas, validando las notas de
# modo que acepten valores
# entre 0 y 20

def leerNumeroEntero(texto, vmin, vmax):
    Nro = int(input(texto))
    while (Nro < vmin) or (Nro > vmax):
        print("ERROR Nro fuera de rango...")
        Nro = int(input("Vuelve a ingresar el número: "))
    return Nro

def leerNumeroReal(texto, vmin, vmax):
    Nro = float(input(texto))
    while (Nro < vmin) or (Nro > vmax):
        print("ERROR Nro fuera de rango...")
        Nro = float(input("Vuelve a ingresar el número: "))
    return Nro

def main():
    print("Se calculará el promedio de 3 notas...")
    nota1 = leerNumeroReal("Ingresa la nota 1: ", 0, 20)
    nota2 = leerNumeroReal("Ingresa la nota 2: ", 0, 20)
    nota3 = leerNumeroReal("Ingresa la nota 3:", 0, 20)
    promedio = (nota1 + nota2 + nota3) / 3
    print("El promedio es " + str(promedio))


main()
