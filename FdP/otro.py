# Problema .- Escriba un programa modular
# para calcular el promedio de
# 3 notas, validando las notas de
# modo que acepten valores
# entre 0 y 20

def leerNota():
    Nota = int(input("Ingrese la nota: "))
    while (Nota < 0) or (Nota > 20):
        print("La nota ingresada no es válida...")
        Nota = int(input("Ingrese la nota: "))
    return Nota

def main():
    print("Se calculará el promedio de 3 notas...")
    nota1 = leerNota()
    nota2 = leerNota()
    nota3 = leerNota()
    promedio = (nota1 + nota2 + nota3) / 3
    print("El promedio es " + str(promedio))


main()
