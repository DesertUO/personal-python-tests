# Implementar las operaciones de las tablas aritméticas
# **********************
# * Tablas aritméticas *
# **********************
# 1. Sumar
# 2. Restar
# 3. Multiplicar
# 4. Dividir
# 5. Salir

# Módulo para hacer una línea de N asterísco
def hacerLinea(N):
    print("*"*N)

# Módulo para ecerrar un texto en asteríscos
def encerrarTexto(texto):
    hacerLinea(len(texto) + 4)
    print("* " + texto + " *")
    hacerLinea(len(texto) + 4)
    
# Títulos de cada tabla
tituloSuma = "Tabla de la Suma"
tituloResta = "Tabla de la Resta"
tituloMultiplicacion = "Tabla de la Multipplicación"
tituloDivision = "Tabla de la División"

# Módulo de la tabla de la suma
def tablaSuma():
    encerrarTexto(tituloSuma)
    
    numero = input("Ingrese un número -> ")
    while (not(numero.isnumeric and (0 < int(numero) <= 10))):
        print("El número ingresado no es válido... debe ser un número entre 1 y 10")
        numero = input("Ingrese un número -> ")
        
    numero = int(numero)
    
    for k in range(1, 13):
        sumaK = numero + k
        print(str(k) + " + " + str(numero) + " = " + str(sumaK))
    
    menu()

# Módulo de la tabla de la resta
def tablaResta():
    encerrarTexto(tituloResta)
    
    numero = input("Ingrese un número -> ")
    while (not(numero.isnumeric and (0 < int(numero) <= 10))):
        print("El número ingresado no es válido... debe ser un número entre 1 y 10")
        numero = input("Ingrese un número -> ")
        
    numero = int(numero)
    
    for k in range(1, 13):
        restaK = k
        print(str(numero + k) + " - " + str(numero) + " = " + str(restaK))
        
    menu()

# Módulo de la tabla de la multiplicación
def tablaMultiplicacion():
    encerrarTexto(tituloMultiplicacion)
    
    numero = input("Ingrese un número -> ")
    while (not(numero.isnumeric and (0 < int(numero) <= 10))):
        print("El número ingresado no es válido... debe ser un número entre 1 y 10")
        numero = input("Ingrese un número -> ")
        
    numero = int(numero)
    
    for k in range(1, 13):
        productK = k * numero
        print(str(numero) + " x " + str(k) + " = " + str(productK))
        
    menu()

# Módulo de la tabla de la división
def tablaDivision():
    encerrarTexto(tituloDivision)
    
    numero = input("Ingrese un número -> ")
    while (not(numero.isnumeric and (0 < int(numero) <= 10))):
        print("El número ingresado no es válido... debe ser un número entre 1 y 10")
        numero = input("Ingrese un número -> ")
        
    numero = int(numero)
    
    for k in range(1, 13):
        cocienteK = k
        print(str(k * numero) + " ÷ " + str(numero) + " = " + str(cocienteK))
    
    menu()

# Módulo del menú principal
def menu():
    titulo = "Tablas aritméticas"
    encerrarTexto(titulo)
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    pregunta = "¿Qué es lo que quiere hacer? -> "

    hacerLinea(len(pregunta))
    opcion = input(pregunta)
    
    while (not(opcion.isnumeric() and (0 < int(opcion) <= 5))):
        print("Ingresaste una opción inválida")
        hacerLinea(len(pregunta))
        opcion = input(pregunta)
        
    opcion = int(opcion) 
    if opcion == 1:
        tablaSuma()
    elif opcion == 2:
        tablaResta()
    elif opcion == 3:
        tablaMultiplicacion()
    elif opcion == 4:
        tablaDivision()
    elif opcion == 5:
        print("Saliendo...")
        return 0

# Iniciar el menu
menu()