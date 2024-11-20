# --- Modulo de tipo función
def NumeroInvertido(Numero:int):
    NumeroAux = Numero
    NumeroInvertido = 0
    NumeroAux1 = Numero
    digit = 0
    while NumeroAux1 > 1:
        NumeroAux1 = NumeroAux1 // 10
        digit += 1
    i = 0
    while i < digit:
        NumeroInvertido = NumeroInvertido * 10 + NumeroAux % 10
        NumeroAux = NumeroAux // 10
        i = i + 1
    return(NumeroInvertido)

def SumaDosNumeros(num1, num2):
    return num1 + num2