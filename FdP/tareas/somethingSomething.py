from Libreria import LeerNroEntero, LeerNroReal
# Escribir una aplicación para realizar operaciones con nros racionales y nros complejos

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

# Módulo para leer un número complejo
def LeerNroRacional(NombreRacional):
    N = int(input("Ingrese numerador del " + NombreRacional + " número racional: "))
    D = int(input("Ingrese denominador del " + NombreRacional + " número racional: "))
    while (D == 0):
        print("ERROR. El denominador no puede ser CERO")
        D = int(input("Ingrese denominador del " + NombreRacional + " número recional"))
    N, D = Simplificar(N, D)
    return N, D

def LeerNroComplejo(NombreComplejo):
    ReZ = int(input("Ingrese la parte real del " + NombreComplejo + " número complejo: "))
    ImZ = int(input("Ingrese la parte imaginaria del " + NombreComplejo + " número complejo: "))
    return ReZ, ImZ

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

# Módulo para escribir un número complejo con la correcta forma: a + bi
def escribirComplejo(Re, Im):
    print(Re if Re != 0 else "", "+" if Im > 0 else (""), Im if Im != 0 else "", "i" if Im != 0 else "")

# Módulos para procesar operaciones con números complejos

# Módulo para procesar sumas
def ProcesarSumarC():
    def Sumar(Re1, Im1, Re2, Im2):
        Re = Re1 + Re2
        Im = Im1 + Im2
        return Re, Im

    # Leer dos números complejos
    R1, I1 = LeerNroComplejo("Primer")
    R2, I2 = LeerNroComplejo("Segundo")

    # Sumar los dos números racionales    
    RR, IR = Sumar(R1, I1, R2, I2)

    # Mostrar el resultado
    print(RR, "+" if IR > 0  else ("" if IR == 0 else "-"), str(IR) + "i" if IR != 0 else "")


# Módulos para procesar restas
def ProcesarRestarC():
    def Restar(Re1, Im1, Re2, Im2):
        Re = Re1 - Re2
        Im = Im1 - Im2
        return Re, Im

    # Leer dos números complejos
    R1, I1 = LeerNroComplejo("Primer")
    R2, I2 = LeerNroComplejo("Segundo")

    # Sumar los dos números racionales    
    RR, IR = Restar(R1, I1, R2, I2)

    # Mostrar el resultado
    escribirComplejo(RR, IR)

# Módulos para procesar operaciones con números complejos
def ProcesarMultiplicarC():
    def Multiplicar(Re1, Im1, Re2, Im2):
        Re = (Re1 * Re2) - (Im1 * Im2)
        Im = (Re1 * Im2) + (Re2 * Im1)
        return Re, Im

    # Leer dos números complejos
    R1, I1 = LeerNroComplejo("Primer")
    R2, I2 = LeerNroComplejo("Segundo")

    # Sumar los dos números racionales    
    RR, IR = Multiplicar(R1, I1, R2, I2)

    # Mostrar el resultado
    escribirComplejo(RR, IR)

# Módulos para procesar operaciones con números complejos
def ProcesarDividirC():
    def Dividir(Re1, Im1, Re2, Im2):
        Re = (Re1 * Re2 + Im1 * Im2) / (Re2 ** 2 + Im2 ** 2)
        Im = (Im1 * Re2 - Re1 * Im2) / (Re2 ** 2 + Im2 ** 2)
        return Re, Im

    # Leer dos números complejos
    R1, I1 = LeerNroComplejo("Primer")
    R2, I2 = LeerNroComplejo("Segundo")

    # Sumar los dos números racionales    
    RR, IR = Dividir(R1, I1, R2, I2)

    # Mostrar el resultado
    escribirComplejo(RR, IR)

def ProcesarConjugarC():
    def Conjugada(Re, Im):
        R = Re
        I = - Im
        return R, I
    
    # Leer el número complejo
    R1, I1 = LeerNroComplejo("un")

    # Hallar su Conjugada
    RR, IR = Conjugada(R1, I1)

    # Mostrar el resultado
    escribirComplejo(RR, IR)

# Módulos para escribir los menús

# Módulo del menú principal
def Menu():
    print("OPERACIONES PRINCIPALES")
    print("==================================")
    print("1.- Números racionales ")
    print("2.- Números complejos ")
    print("3.- Salir ")
    print()

# Módulo del menú de racionales
def MenuRacionales():
    print("OPERACIONES CON NÚMEROS RACIONALES")
    print("==================================")
    print("1.- Sumar ")
    print("2.- Restar ")
    print("3.- Multiplicar ")
    print("4.- Dividir ")
    print("5.- Atras ")
    print()

# Módulo del menú de complejos
def MenuComplejos():
    print("OPERACIONES CON NÚMEROS COMPLEJOS")
    print("==================================")
    print("1.- Sumar ")
    print("2.- Restar ")
    print("3.- Multiplicar ")
    print("4.- Dividir ")
    print("5.- Atras ")
    print()

# #######################################################
#                   Programa principal
# ########################################################

# Módulos para los menús
def operacionesRacionales():
    Opcion = 0
    while (Opcion != 5):
        MenuRacionales()
        Opcion = LeerNroEntero("Ingrese opción --> ", 1, 5)
        if (Opcion == 1):
            ProcesarSumar()
        elif (Opcion == 2):
            ProcesarRestar()
        elif (Opcion == 3):
            ProcesarMultiplicar()
        elif (Opcion == 4):
            ProcesarDividir()

def operacionesComplejos():
    Opcion = 0
    while (Opcion != 5):
        MenuComplejos()
        Opcion = LeerNroEntero("Ingrese opción --> ", 1, 5)
        if (Opcion == 1):
            ProcesarSumarC()
        elif (Opcion == 2):
            ProcesarRestarC()
        elif (Opcion == 3):
            ProcesarMultiplicarC()
        elif (Opcion == 4):
            ProcesarDividirC()

# Módulo del menú principal
def operacionesPrincipales():
    OpcionMain = 0
    while (OpcionMain != 3):
        Menu()
        OpcionMain = LeerNroEntero("Ingrese opción --> ", 1, 3)
        if (OpcionMain == 1):
            operacionesRacionales()
        elif (OpcionMain == 2):
            operacionesComplejos()

operacionesPrincipales()
