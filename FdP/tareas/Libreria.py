# Librería de módulos que pueden ser utilizados en cualquier programa

# Módulos de lectura de números

# Módulo para leer un número entero
def LeerNroEntero(Texto, Minimo, Maximo = 100000000000):
    Nro = int(input(Texto))
    while (Nro < Minimo) or (Nro > Maximo):
        print('Error. Número fuera de rango...')
        Nro = int(input(Texto))
    return Nro

# Módulo para leer un número real
def LeerNroReal(Texto, Minimo, Maximo = 100000000000.0):
    Nro = float(input(Texto))
    while (Nro < Minimo) or (Nro > Maximo):
        print('Error. Número fuera de rango...')
        Nro = float(input(Texto))
    return Nro

# Módulo para determinar el menor de dos números
def MenorDos(A, B):
    return A if A < B else B

# Módulo para determinar el mayor de dos números
def MayorDos(A, B):
    return A if A > B else B
        
# Módulo para intercambiar valores
def Intercambiar(A, B): 
    Temp = A 
    A = B 
    B = Temp 
    return (A, B) 

# Módulo para ordenar dos números
def OrdenarDos(A, B): 
    if A > B:
        A, B = Intercambiar(A,B) 
    return (A, B) 

# --- Modulo Leer Tiempo
def LeerTiempo(Texto):
    print(Texto)
    H = LeerNroEntero('Ingresa Hora: ',0,23)
    M = LeerNroEntero('Ingresa Minuto: ',0,59)
    S = LeerNroEntero('Ingresa Segundo: ',0,59)
    return H,M,S
# --- Modulo Tiempo a Segundos
def TiempoASegundos(HH,MM,SS):
    return HH*3600+MM*60+SS

# --- Modulo para convertir segundos a HH:MM:SS
def SegundosATiempo(TotalSegundos):
    HH = TotalSegundos //3600
    MM = (TotalSegundos %3600)//60
    SS = TotalSegundos % 60
    return HH,MM,SS
# Módulo para leer un punto
def LeerPunto(Texto):
    X = float(input('Ingrese el valor de la coordenada X: '))
    Y = float(input('Ingrese el valor de la coordenada Y: '))
    return X, Y

# Módulo para calcular la distancia entre dos puntos
def Distancia(X1, Y1, X2, Y2):
    return ((X2 - X1)**2 + (Y2 - Y1)**2)**0.5        
