# Actividad 1: Dado un número entero de 3 dígitos, escribir un programa que
# determine el número de veces que aparece el numero 5
# Inicialmente se puede plantear el siguiente algoritmo:
# El patrón que podemos identificar aquí es que, para cada dígito del número,
# debemos verificar si es igual a 5 y luego eliminar ese dígito del número. Al
# trabajar con un número de tres dígitos, este proceso se repite tres veces.
# Identificando las 4 partes de una estructura repetitiva tenemos lo siguiente:
# * Inicialización: contar_5 = 0 y el número ingresado por el usuario.
# * Condición: Mientras el número sea mayor que 0 (num > 0).
# * Bloque de sentencias: Obtenemos el último dígito y verificamos si es igual a 5.
# * Actualización: Dividimos el número por 10 para eliminar el último dígito.

# Sección de evaluación (Actividad 1): En el ejercicio anterior,
# desarrollamos un programa que contaba cuántas veces aparecía el
# número 5 en un número de tres dígitos utilizando un bucle mientras.
# Ahora, tu tarea consiste en reescribir ese código empleando un bucle
# para y, además, generalizarlo para que funcione con un número de n
# dígitos, permitiendo contar cualquier dígito especificado por el usuario.

# Utilizando el while loop
def aparicionDelCincoWhile():
    nro = int(input("Ingrese un número positivo: "))
    while nro <= 0:
        print("El número debe de ser un número entero positivo")
        nro = int(input("Ingrese un número positivo: "))

    digitoAEncontrar = int(input("Ingrese el dígito que quiera contar: "))
    while nro <= 0:
        print("El digito a encontrar debe de ser un número entero positivo")
        digitoAEncontrar = int(input("Ingrese el dígito que quiera contar: "))

    # Contar la cantidad de dígitos
    nroTemp = nro
    digitos = 0
    while nroTemp > 0:
        nroTemp = nroTemp // 10
        digitos += 1

    # Contar el número de apariciones del 5 en nro con un loop while
    contador = 0
    i = 0
    while i <= digitos:
        i += 1
        digito = nro % 10
        if digito == digitoAEncontrar:
            contador += 1

        nro = nro // 10

    print(f"El número de veces que aparece el número {digitoAEncontrar} en {nro} es de {contador}")

# Utilizando el for loop
def aparicionDelCincoFor():
    nro = int(input("Ingrese un número positivo: "))
    while nro <= 0:
        print("El número debe de ser un número entero positivo")
        nro = int(input("Ingrese un número positivo: "))

    digitoAEncontrar = int(input("Ingrese el dígito que quiera contar: "))
    while nro <= 0:
        print("El digito a encontrar debe de ser un número entero positivo")
        digitoAEncontrar = int(input("Ingrese el dígito que quiera contar: "))
    
    # Contar la cantidad de dígitos
    nroTemp = nro
    digitos = 0
    while nroTemp > 0:
        nroTemp = nroTemp // 10
        digitos += 1

    # Contar el número de apariciones del 5 en nro con un loop for
    contador = 0
    for i in range(digitos):
        digito = nro % 10
        if digito == digitoAEncontrar:
            contador += 1

        nro = nro // 10

    print(f"El número de veces que aparece el número {digitoAEncontrar} en {nro} es de {contador}")

# Actividad 2: En uno de los laboratorios de la Carrera de Ingeniería
# Informática se tiene N estudiantes de la asignatura de PENSAMIENTO
# COMPUTACIONAL y M estudiantes de la asignatura de TECNOLOGIAS
# DE LA INFORMACION, para cada estudiante se tiene el promedio final.
# Escribir un programa que calcule el promedio del laboratorio (ambos
# cursos).
# * Entrada de datos: El programa primero solicita al usuario el
# número de estudiantes en PENSAMIENTO COMPUTACIONAL
# (N) y TECNOLOGÍAS DE LA INFORMACIÓN (M). Luego, pide
# ingresar los promedios de cada estudiante de ambos cursos.
# * Cálculo de sumas: Utiliza un bucle for para iterar sobre cada
# curso, sumar los promedios de los estudiantes de cada
# asignatura.
# * Cálculo del promedio global: El promedio del laboratorio se
# obtiene dividiendo la suma total de los promedios entre el número
# total de estudiantes de ambos cursos.
# * Salida: El programa imprime el promedio del laboratorio.

# Sección de evaluación (Actividad 2): En la actividad anterior, el
# ejercicio se realizó utilizando el bucle para. Ahora, tu tarea es reescribir
# ese mismo código utilizando el bucle mientras. Además, debes incluir
# validaciones para asegurarte de que el número de estudiantes de ambos
# cursos y las calificaciones ingresadas sean correctos.

# Módulo para obtener el promedio del laboratorio con loops while
def promedioLabWhile():
    nroEstudianesN = int(input("Ingrese el número de estudiantes de la asignatuda de PC: "))
    while nroEstudianesN <= 0:
        print("El númer de estudiantes no puede ser menor a 0")
        nroEstudianesN = int(input("Ingrese el número de estudiantes de la asignatuda de PC: "))

    nroEstudianesM = int(input("Ingrese el número de estudiantes de la asignatuda de TI: "))
    while nroEstudianesM <= 0:
        print("El númer de estudiantes no puede ser menor a 0")
        nroEstudianesM = int(input("Ingrese el número de estudiantes de la asignatuda de T: "))

    # Para PC
    estudianteN = 0
    sumaPromedioN = 0
    while estudianteN < nroEstudianesN:
        estudianteN += 1
        notaPromedioN = int(input(f"Ingrese el promedio del estudiante {estudianteN} en PC: "))
        while (notaPromedioN < 0) or (notaPromedioN > 20):
            print("La nota debe de estar entre 0 y 20")
            notaPromedioN = int(input(f"Ingrese el promedio del estudiante {estudianteN} en PC: "))
        sumaPromedioN += notaPromedioN

    promedioLabN = sumaPromedioN / nroEstudianesN

    # Para TI
    estudianteM = 0
    sumaPromedioM = 0
    while estudianteM < nroEstudianesM:
        estudianteM += 1
        notaPromedioM = int(input(f"Ingrese el promedio del estudiante {estudianteM} en PC: "))
        while (notaPromedioM < 0) or (notaPromedioM > 20):
            print("La nota debe de estar entre 0 y 20")
            notaPromedioM = int(input(f"Ingrese el promedio del estudiante {estudianteM} en PC: "))
        sumaPromedioM += notaPromedioM
    
    promedioLabM = sumaPromedioM / nroEstudianesM

    promedioLab = (sumaPromedioN + sumaPromedioM) / (nroEstudianesN + nroEstudianesM)
    print(f"El promedio del laboratorio es {promedioLab}")
    return promedioLab

# Módulo para obtener el promedio del laboratorio con loops for
def promedioLabFor():
    nroEstudianesN = int(input("Ingrese el número de estudiantes de la asignatuda de PC: "))
    while nroEstudianesN <= 0:
        print("El númer de estudiantes no puede ser menor a 0")
        nroEstudianesN = int(input("Ingrese el número de estudiantes de la asignatuda de PC: "))

    nroEstudianesM = int(input("Ingrese el número de estudiantes de la asignatuda de TI: "))
    while nroEstudianesM <= 0:
        print("El númer de estudiantes no puede ser menor a 0")
        nroEstudianesM = int(input("Ingrese el número de estudiantes de la asignatuda de T: "))

    # Para PC
    sumaPromedioN = 0
    for estudianteN in range(nroEstudianesN):
        notaPromedioN = int(input(f"Ingrese el promedio del estudiante {estudianteN + 1} en PC: "))
        while (notaPromedioN < 0) or (notaPromedioN > 20):
            print("La nota debe de estar entre 0 y 20")
            notaPromedioN = int(input(f"Ingrese el promedio del estudiante {estudianteN + 1} en PC: "))
        sumaPromedioN += notaPromedioN
    # Tal vez
    promedioLabN = sumaPromedioN / nroEstudianesN

    # Para TI
    sumaPromedioM = 0
    for estudianteM in range(nroEstudianesM):
        notaPromedioM = int(input(f"Ingrese el promedio del estudiante {estudianteM + 1} en PC: "))
        while (notaPromedioM < 0) or (notaPromedioM > 20):
            print("La nota debe de estar entre 0 y 20")
            notaPromedioM = int(input(f"Ingrese el promedio del estudiante {estudianteM + 1} en PC: "))
        sumaPromedioM += notaPromedioM
    # Tal vez
    promedioLabM = sumaPromedioM / nroEstudianesM

    promedioLab = (sumaPromedioN + sumaPromedioM) / (nroEstudianesN + nroEstudianesM)
    print(f"El promedio del laboratorio es {promedioLab}")
    return promedioLab

# Actividad 3: En el curso de Pensamiento Computacional, se decidió
# cobrar una cuota de M soles a N compañeros para celebrar el fin de
# semestre. El docente, para premiar a los alumnos aprobados, decidió
# aplicar un descuento en la cuota:
# * Un 50% de descuento para los alumnos con nota 20.
# * Un 30% de descuento para los alumnos con nota mayor a 17.
# * Implementa un programa en Python que permita al delegado cobrar a
# sus compañeros, aplicar los descuentos correspondientes y calcular el
# monto total recaudado.
# * Considera validar que las notas y el monto sea un valor valido

def cobrarCuotaWhile():
    # Obterner el monto base
    M = int(input("Ingrese el monto base que se va a cobrar: "))
    while M < 0:
        print("El monto no puede ser menor a 0...")
        M = int(input("Ingrese el monto base que se va a cobrar: "))
    
    # Obtener el número de compañeros a cobrar
    N = int(input("Ingrese el número de compañeros: "))
    while M <= 0:
        print("El numero de compañeros no puede ser 0 ni menor a 0...")
        N = int(input("Ingrese el número de compañeros: "))
    
    totalRecaudado = 0
    i = 0
    while i < N:
        i += 1
        print(f"Cobrando al compañero nro. {i}")
        nota = int(input("La nota del compañero: "))
        while (nota < 0) or (nota > 20):
            print("La nota no puede ser menor a 0 ni mayor a 20")
            nota = int(input("La nota del compañero: "))

        if nota == 20:
            descuento = 0.5
        elif nota >= 17:
            descuento = 0.3
        else:
            descuento = 0
        montoCobradoI = M - M*descuento
        print(f"Se cobró {montoCobradoI}")
        totalRecaudado += montoCobradoI
    print(f"Se recaudó un total de S/.{totalRecaudado}")

def cobrarCuotaFor():
    # Obterner el monto base
    M = int(input("Ingrese el monto base que se va a cobrar: "))
    while M < 0:
        print("El monto no puede ser menor a 0...")
        M = int(input("Ingrese el monto base que se va a cobrar: "))
    
    # Obtener el número de compañeros a cobrar
    N = int(input("Ingrese el número de compañeros: "))
    while M <= 0:
        print("El numero de compañeros no puede ser 0 ni menor a 0...")
        N = int(input("Ingrese el número de compañeros: "))

    totalRecaudado = 0
    for i in range(N):
        print(f"Cobrando al compañero nro. {i + 1}")
        nota = int(input("La nota del compañero: "))
        while (nota < 0) or (nota > 20):
            print("La nota no puede ser menor a 0 ni mayor a 20")
            nota = int(input("La nota del compañero: "))

        if nota == 20:
            descuento = 0.5
        elif nota >= 17:
            descuento = 0.3
        else:
            descuento = 0
        montoCobradoI = M - M*descuento
        print(f"Se cobró {montoCobradoI}")
        totalRecaudado += montoCobradoI
    print(f"Se recaudó un total de S/.{totalRecaudado}")

# Ejercicios adicionales (Opcional)
# * 1. Escribe un programa que solicite al usuario ingresar un número entero n y
# dibuje un triángulo de asteriscos de altura n.
# * 2. Escribe un programa que solicite una palabra o frase y cuente cuántas vocales
# (a, e, i, o, u) contiene. El programa debe mostrar el número total de vocales.
# * 3. Escribe un programa que solicite al usuario ingresar un número entero positivo
# y sume por separado los números pares e impares desde 1 hasta ese número.
# El programa debe mostrar ambas sumas por separado.
# * 4. Escribe un programa que imprima los primeros n términos de la serie de
# Fibonacci. La serie comienza con 0 y 1, y cada término subsiguiente es la suma
# de los dos anteriores.

# ------->
# 1.
def dibujarTriangulo():
    n = int(input("Ingrese la altura del triángulo: "))
    while n <= 0:
        print("La altura no puede ser menor o igual a 0...")
        n = int(input("Ingrese la altura del triángulo: "))
    
    print()
    
    h = 0
    while h < n:
        h += 1
        print("*"*h)

# 2.
def contarVocales():
    texto = input("Ingrese una palabra o frase\n")
    nroVocales = 0
    for i in range(len(texto)):
        cAct = texto[i]
        if (cAct == "a") or (cAct == "e") or (cAct == "i") or (cAct == "o") or (cAct == "u") or (cAct == "A") or (cAct == "E") or (cAct == "I") or (cAct == "O") or (cAct == "U"):
            nroVocales += 1
    print(f"La palabra/texto contiene {nroVocales} vocales")

# 3. 
def sumarParImpar():
    n = int(input("Ingrese un número entero positivo: "))
    while n <= 0:
        print("El número no puede ser menor o igual a 0")
        n = int(input("Ingrese un número entero positivo: "))

    sumaPar = 0
    sumaImpar = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            sumaPar += i
        else:
            sumaImpar += i
    
    print(f"La suma de los números pares de 1 hasta {n} es {sumaPar}")
    print(f"La suma de los números impares de 1 hasta {n} es {sumaImpar}")

# 4.
def printTermFibonacci():
    nroTerm = int(input("Ingrese el número de términos a imprimir: "))
    while nroTerm <= 0:
        print("El número de términos debe ser un número entero positivo.")
        nroTerm = int(input("Ingrese el número de términos a imprimir: "))

    term1 = 0
    term2 = 1

    print("Serie Fibonacci:")
    for i in range(nroTerm):
        print(str(term1) + " ")
        termAux = term1
        term1 = term2
        term2 = termAux + term2

# --------------------------------------------------
funcionesI = [aparicionDelCincoWhile, aparicionDelCincoFor, promedioLabWhile, promedioLabFor, cobrarCuotaWhile, cobrarCuotaFor, dibujarTriangulo, contarVocales, sumarParImpar, printTermFibonacci]

# Menú para probar todos los módulos:
def menuLista():
    print("---------------Menú---------------")
    print("Se tienen las siguientes opciones:")
    print("*" * 30)
    for i in range(len(funcionesI)):
        print(f"{i + 1}. {funcionesI[i].__name__}")
    print(f"{len(funcionesI) + 1}. Salir")

def menu():
    opcion = 0
    while opcion != (len(funcionesI) + 1):
        menuLista()
        # Sin try/except
        print("*" * 30)
        opcion = int(input("¿Qué es lo que quiere hacer?: "))
        while (opcion <= 0) or (opcion > (len(funcionesI) + 1)):
            print("Elige una opción válida...")
            opcion = int(input(""))
        if opcion == len(funcionesI) + 1:
            print("Gracias por usar este menu...")
        else:
            funcionesI[opcion - 1]()

menu()