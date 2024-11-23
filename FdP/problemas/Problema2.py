from libreria_1 import *
# Escribir un programa modular que dado 2 nros racionales permita realizar las operaciones de:
# Sumar, restar, multiplicar y dividir.

# Módulo de MCD
def MCD(Nro1: int, Nro2: int):
    R = Nro1 % Nro2
    while (R != 0):
        Nro1 = Nro2
        Nro2 = R
        R = Nro1 % Nro2
    return Nro2

# Módulo para simplificar
def Simplificar(Nro1, Nro2):
    M = MCD(Nro1, Nro2)
    Nro1 = Nro1 // M
    Nro2 = Nro2 // M
    return Nro1, Nro2

# Módulo para leer un número racional
def LeerNroRacional(NombreRacional):
    N = int(input("Ingrese numerador del " + NombreRacional + " número racional: "))
    D = int(input("Ingrese denominador del " + NombreRacional + " número racional: "))
    while (D == 0):
        print("ERROR. El denominador no puede ser CERO")
        D = int(input("Ingrese denominador del " + NombreRacional + " número recional"))
    N, D = Simplificar(N, D)
    return N, D

# Módulos para procesar operaciones con números racionales

# Modulo para procesar suma
def ProcesarSumar():
    def Sumar(N1, D1, N2, D2):
        NS = N1 * D2 + N2 *D1
        DS = D1 * D2
        NS, DS = Simplificar(NS, DS)
        return NS, DS

    # Leer dos números racionales
    N1, D1 = LeerNroRacional("Primer")
    N2, D2 = LeerNroRacional("Segundo")

    # Sumar los dos números racionales    
    NR, DR = Sumar(N1, D1, N2, D2)

    # Mostrar el resultado
    print(NR, "/", DR)

# Modulo para procesar resta
def ProcesarRestar():
    def Restar(N1, D1, N2, D2):
        NS = N1 * D2 - N2 *D1
        DS = D1 * D2
        NS, DS = Simplificar(NS, DS)
        return NS, DS

    # Leer dos números racionales
    N1, D1 = LeerNroRacional("Primer")
    N2, D2 = LeerNroRacional("Segundo")

    # Sumar los dos números racionales    
    NR, DR = Restar(N1, D1, N2, D2)

    # Mostrar el resultado
    print(NR, "/", DR)

# Modulo para procesar multiplicación
def ProcesarMultiplicar():
    def Multiplicar(N1, D1, N2, D2):
        NS = N1 * N2
        DS = D1 * D2
        NS, DS = Simplificar(NS, DS)
        return NS, DS

    # Leer dos números racionales
    N1, D1 = LeerNroRacional("Primer")
    N2, D2 = LeerNroRacional("Segundo")

    # Sumar los dos números racionales    
    NR, DR = Multiplicar(N1, D1, N2, D2)

    # Mostrar el resultado
    print(NR, "/", DR)

# Modulo para procesar división
def ProcesarDividir():
    def Dividir(N1, D1, N2, D2):
        NS = N1 * D2
        DS = D1 * N2
        NS, DS = Simplificar(NS, DS)
        return NS, DS

    # Leer dos números racionales
    N1, D1 = LeerNroRacional("Primer")
    N2, D2 = LeerNroRacional("Segundo")

    # Sumar los dos números racionales    
    NR, DR = Dividir(N1, D1, N2, D2)

    # Mostrar el resultado
    print(NR, "/", DR)

# Módulo Menu

def Menu():
    print("OPERACIONES CON NÚMEROS RACIONALES")
    print("==================================")
    print("1.- Sumar ")
    print("2.- Restar ")
    print("3.- Multiplicar ")
    print("4.- Dividir ")
    print("5.- Salir ")
    print()

# #######################################################
#                   Programa principal
# ########################################################
Opcion = 0
while (Opcion != 5):
    Menu()
    Opcion = LeerNroEntero("Ingrese opción --> ", 1, 5)
    if (Opcion == 1):
        ProcesarSumar()
    elif (Opcion == 2):
        ProcesarRestar()
    elif (Opcion == 3):
        ProcesarMultiplicar()
    elif (Opcion == 4):
        ProcesarDividir()