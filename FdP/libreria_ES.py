def LeerNroEntero(msg, vmin = -9999999999999, vmax = 9999999999999) -> int:
    while True:
        try:
            Num = int(input(msg))
            if Num < vmin or Num > vmax:
                print(f"Por favor ingrese un número que este entre {vmin} y {vmax}.")
            else:
                return Num
        except ValueError:
            print("ERROR. El número debe ser uno entero.")

def LeerNroReal(msg, vmin = -9999999999999, vmax = 9999999999999) -> float:
    while True:
        try:
            Num = float(input(msg))
            if Num < vmin or Num > vmax:
                print(f"Por favor ingrese un número que este entre {vmin} y {vmax}.")
            else:
                return Num
        except ValueError:
            print("ERROR. El número debe ser uno real.")

def intercambiarDos(num1, num2) -> tuple[float, float]:
    numAux = num1
    num1 = num2
    num2 = numAux
    return num1, num2

def mayorDos(num1, num2) -> float:
    if num1 >= num2:
        numMayor = num1
    else:
        numMayor = num2
    return numMayor

def ordenarDos(num1, num2) -> tuple[float, float]:
    return (num1 + num2 - mayorDos(num1, num2)), mayorDos(num1, num2)

def leerPunto(msg: str = "") -> tuple[float, float]:
    print(msg)
    x, y = LeerNroReal("Ingrese la coordenada x: "), LeerNroReal("Ingrese la coordenada y: ")
    return x, y

def calcDistancia(x1: float, y1: float, x2: float, y2: float) -> float:
    return (((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)