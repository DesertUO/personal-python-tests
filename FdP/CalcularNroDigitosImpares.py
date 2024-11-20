'''Determinar el Nro de dígiros impares de un Nro de 3 dígitos.'''
'''Modificado para aceptar números de n dígitos'''

# --- Obetner Datos (número)
NumeroOriginal = int(input("Ingrese un número de 3 dígitos para obtener el número de dígitos impares del número: "))
# --- Procesar Datos (Obtener el número de dígitos impares del número ingresado)
NumeroAux = NumeroOriginal
NumeroDigitosImpares = 0
NumeroAux1 = NumeroOriginal
digit = 0
while NumeroAux1 > 0:
    NumeroAux1 = NumeroAux1 // 10
    digit += 1
while NumeroAux > 0:
    NumeroDigitosImpares = NumeroDigitosImpares + NumeroAux % 2
    NuneroAux = NumeroAux // 10
# --- Mostrar Resultados
print("El número ", NumeroOriginal, " tiene ", NumeroDigitosImpares, " dígitos impares.")
