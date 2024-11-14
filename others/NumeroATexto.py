# En español (In Spanish)

## Errores asdfbghnymgiuqwertyuiop

# Números de 1 cifra
def DigitoATexto(N: int):
    if 0 <= N <= 9:
        if N == 0:
            Text = ""
        elif N == 1:
            Text = "uno"
        elif N == 2:
            Text = "dos"
        elif N == 3:
            Text = "tres"
        elif N == 4:
            Text = "cuatro"
        elif N == 5:
            Text = "cinco"
        elif N == 6:
            Text = "seis"
        elif N == 7:
            Text = "siete"
        elif N == 8:
            Text = "ocho"
        elif N == 9:
            Text = "nueve"

        return Text
    else:
        raise Exception("El número no es un dígito: 0 <= N <= 9")

# Números de 2 cifras
def DecenaATexto(N: int):
    U, D = N % 10, N // 10
    if D == 0:
        Text = "cero" if (U == 0) else DigitoATexto(N)
    elif D == 1:
        if U == 0:
            Text = "diez"
        elif U == 1:
            Text = "once"
        elif U == 2:
            Text = "doce"
        elif U == 3:
            Text = "trece"
        elif U == 4:
            Text = "catorce"
        elif U == 5:
            Text = "quince"
        elif U == 6:
            Text = "dieciseis"
        elif U == 7:
            Text = "diecisiete"
        elif U == 8:
            Text = "dieciocho"
        elif U == 9:
            Text = "diecinueve"
    elif D == 2:
        Text = "veinte" if (U == 0) else "veinti"
        Text = (Text) if (U == 0) else (Text + DigitoATexto(U))
    elif D == 3:
        Text = "treinta"
    elif D == 4:
        Text = "cuarenta"
    elif D == 5:
        Text = "cincuenta"
    elif D == 6:
        Text = "sesenta"
    elif D == 7:
        Text = "setenta"
    elif D == 8:
        Text = "ochenta"
    elif D == 9:
        Text = "noventa"
    Text = Text if (D == 0 or D == 1 or D == 2) else (Text + " y " + DigitoATexto(U))

    return Text

# Números de 3 cifras
def CentenaATexto(N: int):
    U, D, C = N % 10, (N // 10) % 10, N // 100

    if C == 0:
        Text = DecenaATexto(D * 10 + U)
    elif C == 1:
        Text = "cien" if (U == 0 and D == 0) else ("ciento" + DecenaATexto(N % 100))
    elif C == 2:
        Text = "docientos"
    elif C == 3:
        Text = "trescientos"
    elif C == 4:
        Text = "cuatrocientos"
    elif C == 5:
        Text = "quinientos"
    elif C == 6:
        Text = "seiscientos"
    elif C == 7:
        Text = "setecientos"
    elif C == 8:
        Text = "ochocientos"
    elif C == 9:
        Text = "novecientos"
        
    if not (C == 0 or C == 1):
        Text = Text + " " + DecenaATexto(N % 100)
    
    return Text

# Números de 4 cifras a 6 cifras
def MillarATexto(N: int):
    U, D, C, M = N % 10, (N // 10) % 100, (N // 100) % 10, N // 1000

    Text = "" if (M == 0) else ("mil" if (M == 1) else (CentenaATexto(M) + "mil"))
    Text = Text if (U == 0 and D == 0 and C == 0) else (Text + " " + CentenaATexto(N % 1000))
    return Text

# Hasta 999'999
def ConvertirNroATexto(N: int):
    return MillarATexto(N)

# Test del método para convertir números naturales a su forma de palabras
Num = int(input("Ingrese un número: "))
print(ConvertirNroATexto(Num))