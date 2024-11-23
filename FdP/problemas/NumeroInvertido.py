'''Escribir un algorítmo que dado un número de 3 dígios invierta el orden de sus dígitos.'''
'''Ha sido modificado para aceptar números de n dígitos.'''

# --- Obtener Datos (Obtener Número)
NumeroOriginal = int(input("Ingrese un número de n dígitos para obtener el número invertido: "))
# --- Procesar Datos (Invertir Número)
NumeroAux = NumeroOriginal
NumeroInvertido = 0
NumeroAux1 = NumeroOriginal
digit = 0
while NumeroAux1 > 1:
    NumeroAux1 = NumeroAux1 // 10
    digit += 1
i = 0
while i < digit:
    NumeroInvertido = NumeroInvertido * 10 + NumeroAux % 10
    NumeroAux = NumeroAux // 10
    i = i + 1
# --- Mostrar Resultados
print("Dado el número ingresado: ", NumeroOriginal, ", el número invertido viene a ser: ", NumeroInvertido)
