def HacerLinea(N, simbolo = "*"):
    print(simbolo * N)

def EncerrarTexto(Texto, simbolo = "*"):
    HacerLinea(len(Texto) + 4, simbolo)
    print(simbolo + " " + Texto + " " + simbolo)
    HacerLinea(len(Texto) + 4, simbolo)

def LeerNroEntero(msg, vmin = -9999999999999999, vmax  = 9999999999999999):
    Nro = input(msg)
    while (int(Nro) < vmin) or (int(Nro) > vmax):
        Nro = input(msg)
    Nro = int(Nro)
    return Nro

def LeerNroReal(msg, vmin = -9999999999999999, vmax  = 9999999999999999):
    Nro = input(msg)
    while (float(Nro) < vmin) or (float(Nro) > vmax):
        Nro = input(msg)
    Nro = float(Nro)
    return Nro

def Intercambiar(Nro1, Nro2):
    NroAux = Nro1
    Nro1 = Nro2
    Nro2 = NroAux
    return Nro1, Nro2

def MayorDos(Nro1, Nro2):
    return (Nro1 if (Nro1 > Nro2) else Nro2)

def MenorDos(Nro1, Nro2):
    return Nro1 + Nro2 - MayorDos(Nro1, Nro2)

def OrdenarDos(Nro1, Nro2):
    return MenorDos(Nro1, Nro2), MayorDos(Nro1, Nro2)

def LeerTiempo(msg):
    print(msg)
    H = LeerNroEntero("Ingrese las horas: ", 0, 24)
    M = LeerNroEntero("Ingrese los minutos: ", 0, 59)
    S = LeerNroEntero("Ingrese los segundos: ", 0, 59)
    return H, M, S

def TiempoASeg(H, M, S):
    return H * 3600 + M * 60 + S

def SegATiempo(Seg):
    H = Seg // 3600
    M = (Seg % 3600) // 60
    S = Seg % 60
    return H, M, S

def LeerPunto(msg):
    print(msg)
    x = LeerNroReal("Ingrese la coordenada x: ")
    y = LeerNroReal("Ingrese la coordenada y: ")
    return x, y

def Distancia(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
