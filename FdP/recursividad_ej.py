from libreria_ES import LeerNroEntero

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
# Leer los datos (número de discos)
nDiscos = LeerNroEntero("Ingrese el número de discos: ", 1)
# Resolver el problema para N discos
Hanoi(nDiscos)