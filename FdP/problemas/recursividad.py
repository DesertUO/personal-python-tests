from libreria_ES import leerNroEntero

# Módulos
# Módulo para calcular el factorial de N: N!
def factorial(N):
    # Caso base
    if N == 0:
        return 1
    # Caso recurrente
    return N * factorial(N - 1)

# Módulo para determinar el número de dígitos de N
def digitos(N):
    # Caso base 
    if N < 10:
        return 1
    # Caso recurrente
    return 1 + digitos(N // 10)

# Módulo para calcular el valor de de a * b
def mult(a, b):
    # Caso base
    if b == 0:
        return 0
    # Caso recurrent
    return a + mult(a, b - 1)

# Módulo para calcular el valor de x ^ N
def pot(x, N):
    # Caso base
    if N == 0:
        return 1
    # Caso recurrente
    return x * pot(x, N - 1)

# Módulo para convertir un número decimal a base binaria
def DecABin(N):
    # Caso base
    if N <= 1:
        return N
    # Caso recurrente
    return N % 2 + 10 * DecABin(N // 2)

# Módulo para calcular el MCD de dos números
def MCD(num_1, num_2):
    # Con num_1 > num_2
    # Caso base
    if num_1 % num_2 == 0:
        return num_2
    # Caso recurrente
    return MCD(num_2, num_1 % num_2)

# Módulo para calcular el N-ésimo término de la serie de Fibonacci
def fib(N):
    # Caso base
    if N <= 2:
        return N - 1
    # Caso recurrente
    return fib(N - 1) + fib(N - 2)

# Problema.- Escribir una aplicación para determinar los movimientos que se deben efectuar
# en el problema de las Torres de Hanoi.

# Módulo del procedimiento de Hanoi
def Hanoi(N = 6, Inicio = 1, Final = 3):
    if (N == 1):
        print(f"Mover de {Inicio} a {Final}")
    else:
        Aux = 6 - Inicio - Final
        Hanoi(N - 1, Inicio, Aux)
        Hanoi(1, Inicio, Final)
        Hanoi(N - 1, Aux, Final)


# Probar cada módulo (Programa principal)
def Test():
    # Probar las operaciones
    # Leer los números para realizar las operaciones
    Numero_1 = leerNroEntero("Ingrese un número entero no negativo: ", 0)
    Numero_2 = leerNroEntero("Ingrese otro número entero no negativo: ", 0)
    # Realizar las operaciones
    print(f"El factorial de {Numero_1} es {factorial(Numero_1)}")
    print(f"El número de dígitos de {Numero_1} es {digitos(Numero_1)}")
    print(f"El valor de la expresión {Numero_1} * {Numero_2} es {mult(Numero_1, Numero_2)}")
    print(f"El valor de la expresión {Numero_1}^{Numero_2} es {pot(Numero_1, Numero_2)}")

    # Probar el módulo de MCD
    Numero_1 = leerNroEntero("Ingrese un número entero no negativo: ", 0)
    Numero_2 = leerNroEntero("Ingrese otro número entero no negativo: ", 0)
    print(f"EL MCD de {Numero_1} y {Numero_2} es {MCD(Numero_1, Numero_2)}")

    # Probar la conversión de decimal a binario
    NumeroDec = leerNroEntero("Ingrese un número decimal: ", 0)
    print(f"El número decimal {NumeroDec} es {DecABin(NumeroDec)} en base 2")

    # Probar el n-ésimo térmnio de la serie de Fibonacci
    nTermino = leerNroEntero("Ingrese el término desesado: ", 0)
    print(f"EL {nTermino}-ésimo término de la serie de fibonacci es {fib(nTermino)}")

    # Probar el problema de las torres de Hanoi
    print("Problema de las Torres de Hanoi")
    # Leer los datos (número de discos)
    nDiscos = leerNroEntero("Ingrese el número de discos: ", 1)
    # Resolver el problema para N discos
    Hanoi(nDiscos)

Test()