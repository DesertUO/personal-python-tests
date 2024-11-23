# --- Se tiene las fichas de seguimiento de los N estudiantes de la EPIIS, para c/u se tiene las M asignaturas
# --- cursadas con sus respectivas notas. Escribir un algorítmo que determine:
# --- - El nro de asig. aprobadas de c/estudiante
# --- - El promedio de notas correspondientes a las asignaturas aprobadas por c/estudiante

# --- Leer los datos (número de alumnos de la EPIIS)
N = int(input("Ingrese el número de estudiantes de la EPIIS: "))
while (N <= 0):
    print("El número de empleados debe ser mayor que cero...")
    N = int(input("Ingrese el número de estudiantes de la EPIIS: "))
# --- Leer el número de asignaturas cursadas por c/estudiante
for i in range(1, N + 1):
    M = int(input("Ingrese el número de asignaturas cursadas por el estudiante " + str(i) +": "))
    while (M <= 0):
        print("El número de asignaturas cursadas debe ser mayor que cero...")
        M = int(input("Ingrese el número de asignaturas cursadas por c/estudiante: "))
    AsigAprob = 0
    AsigDesaprob = 0
    NotaSum = 0
    # --- Leer las notas de c/asignatura
    for j in range(1, M + 1):
        Nota = float(input("Ingrese la nota del alumno " + str(i) + " de la asignatura " + str(j) + ": "))
        while not((0 <= Nota) and (Nota <= 20)):
            print("La nota debe ser un número entre 0 y 20")
            Nota = float(input("Ingrese la nota del alumno " + str(i) + " de la asignatura " + str(j) + ": "))
        # --- Determinar si la nota es aprobatoria o no
        if (Nota >= 13.5):
            AsigAprob += 1
            print("Asignatura " + str(j) + " APROBADA")
        else:
            AsigDesaprob += 1
            print("Asignatura " + str(j) + " DESAPROBADA")
        # --- Acumular las notas
        NotaSum += Nota
    # --- Mostrar las asignaturas aprobadas y desaprobadas
    print("El estudiante " + str(i) + " aprobó " + str(AsigAprob) + " asignaturas")
    print("El estudiante " + str(i) + " deaprobó " + str(AsigDesaprob) + " asignaturas")
    # --- Calcular y mostrar el promedio
    Promedio = NotaSum / M
    PromedioEnt = float(int(Promedio))
    print(PromedioEnt)
    PromedioDec = Promedio - PromedioEnt
    if (PromedioDec >= 0.5):
        PromedioRed = PromedioEnt + 1
    else:
        PromedioRed = PromedioEnt
    print("El estudiante " + str(i) + " tiene un promedio final de " + str(PromedioEnt))
