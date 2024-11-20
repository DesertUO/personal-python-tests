'''
##############################################################
Programa que dado dos números racionales permita
efectuar las operaciones: Sumar, Restar, Multiplicar y dividir
##############################################################
'''  
from Libreria import * 
# Módulo MCD
def MCD(A, B):
    R = A % B
    while (R != 0):
        A = B
        B = R
        R = A % B
    return B

# Módulo simplificar
def Simplificar(A, B):
    M = MCD(A, B)
    A = A // M
    B = B // M
    return A, B


# Módulo Leer número racional
def LeerNroRacional(Texto):
    N = int(input('Ingrese numerador del '+Texto+' número racional: '))
    D = int(input('Ingrese denominador del '+Texto+' número racional: '))
    while (D == 0):
        print('ERROR. El denominador no puede ser CERO')
        D = int(input('Ingrese denominador del '+Texto+' número recional'))
    N, D = Simplificar(N, D)
    return N, D

# Módulo procesar Sumar nro racionales

def ProcesarSumar():

    def Sumar(N1, D1, N2, D2):
        NS = N1 * D2 + N2 *D1
        DS = D1 * D2
        NS, DS = Simplificar(NS, DS)
        return NS, DS

    # -- Leer dos números racionales
    N1, D1 = LeerNroRacional('Primer')
    N2, D2 = LeerNroRacional('Segundo')

    # -- Sumar los dos números racionales    
    NR, DR = Sumar(N1, D1, N2, D2)

    # --  Mostrar el resultado
    print(NR, '/', DR)

# Módulo Menu

def Menu():
    print('OPERACIONES CON NÚMEROS RACIONALES')
    print('==================================')
    print('1.- Sumar ')
    print('2.- Restar ')
    print('3.- Multiplicar ')
    print('4.- Dividir ')
    print('5.- FIN ')
    print()

# #######################################################
#                   Programa principal
# ########################################################
Opcion = 0
while (Opcion != 5):
    Menu()
    Opcion = LeerNroEntero('Ingrese opción --> ', 1, 5)
    if (Opcion == 1):
        ProcesarSumar()
    elif (Opcion == 2):
        ProcesarRestar()
    elif (Opcion == 3):
        ProcesarMultiplicar()
    elif (Opcion == 4):
        ProcesarDividir()
    

