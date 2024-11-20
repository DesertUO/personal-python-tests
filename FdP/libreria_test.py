# def hacerLinea(N, simbolo = "*"):
#     print(simbolo * N)
    
# def encerrarTexto(texto, simbolo = "*"):
#     hacerLinea(len(texto) + 4, simbolo)
#     print(simbolo + " " + texto + " " + simbolo)
#     hacerLinea(len(texto) + 4, simbolo)

# Módulo de leer un número entero
def leerNumeroEntero(texto, vmin, vmax):
    Nro = int(input(texto))
    while (Nro < vmin) or (Nro > vmax):
        print("ERROR Nro fuera de rango...")
        Nro = int(input("Vuelve a ingresar el número: "))
    return Nro

# Módulo de leer un número real
def leerNumeroReal(texto, vmin, vmax):
    Nro = float(input(texto))
    while (Nro < vmin) or (Nro > vmax):
        print("ERROR Nro fuera de rango...")
        Nro = float(input("Vuelve a ingresar el número: "))
    return Nro

# Determinar el número mayor
def mayorNro(nro1, nro2):
    if nro1 >= nro2:
        return nro1
    else:
        return nro2

# Determinar número menor
def menorNro(nro1, nro2):
    return nro1 + nro2 - mayorNro(nro1, nro2)

# Módulo para intercambiar 2 nros
def intercambiarNros(nro1, nro2):
    nroAux = nro1
    nro1 = nro2
    nro2 = nroAux
    return nro1, nro2

# Módulo para ordenar 2 nros
def ordenarNros(nro1, nro2):
    if nro1 > nro2:
        intercambiarNros(nro1, nro2)
    return nro1, nro2
