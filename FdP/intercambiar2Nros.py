from problemas.libreria_test import *

def main():
    N1 = leerNumeroReal("Ingrese el Nro1: ", 0, 9999999999999999999)
    N2 = leerNumeroReal("Ingrese el Nro2: ", 0, 9999999999999999999)
    N3 = leerNumeroReal("Ingrese el Nro3: ", 0, 9999999999999999999)

    N1, N2 = ordenarNros(N1, N2)
    N2, N3 = ordenarNros(N2, N3)
    N1, N2 = ordenarNros(N1, N2)

    print(N1, N2, N3)

main()
