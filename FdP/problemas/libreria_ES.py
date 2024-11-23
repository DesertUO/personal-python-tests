# Similar a lo hecho en clase bruh. Agregué los "-> type" y algunas otras cosas (si no recuerdo).

# Módulo para leer números enteros
def leerNroEntero(msg, vmin = -9999999999999, vmax = 9999999999999) -> int:
    Num = int(input(msg))
    while Num < vmin or Num > vmax:
            print(f"Por favor ingrese un número entero que este entre {vmin} y {vmax}.")
            Num = int(input(msg))
    return Num

# Módulo para leer números reales
def leerNroReal(msg, vmin = -9999999999999, vmax = 9999999999999) -> float:
    Num = float(input(msg))
    while Num < vmin or Num > vmax:
            print(f"Por favor ingrese un número real que este entre {vmin} y {vmax}.")
            Num = float(input(msg))
    return Num

# Módulo para intercambiar el orden de 2 números
def intercambiarDos(num1, num2) -> tuple[float, float]:
    numAux = num1
    num1 = num2
    num2 = numAux
    return num1, num2

# Módulo hallar el mayor de 2 números (?)
def mayorDos(num1, num2) -> float:
    if num1 >= num2:
        numMayor = num1
    else:
        numMayor = num2
    return numMayor

# Módulo para ordenar 2 números
def ordenarDos(num1, num2) -> tuple[float, float]:
    return (num1 + num2 - mayorDos(num1, num2)), mayorDos(num1, num2)

# Módulo para leer puntos del plano 2D
def leerPunto(msg: str = "") -> tuple[float, float]:
    print(msg)
    x, y = leerNroReal("Ingrese la coordenada x: "), leerNroReal("Ingrese la coordenada y: ")
    return x, y

# Módulo para calcular la distancia entre 2 puntos
def distancia(x1: float, y1: float, x2: float, y2: float) -> float:
    return (((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)