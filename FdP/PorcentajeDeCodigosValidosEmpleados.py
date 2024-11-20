# --- ASdasdasd

# --- Leer los datos (nro de empleados)
NroEmp = int(input("Ingrese el número de empleados: "))
while (NroEmp <= 0):
    print("El número de empleados debe ser mayor a cero")
    NroEmp = int(input("Ingrese el número de empleados: "))
# --- Buscar a los nros los dígitos primos
CodigosValidos = 0
for i in range(1, NroEmp + 1):
    NroDigPrimos = 0
    # --- Leer código del empleado
    Codigo = int(input("Ingrese el código del empleado " + str(i) + ": "))
    while not ((1000 <= Codigo) and (Codigo <= 9999)):
        print("El código del empleado debe ser un número de 4 cifras")
        Codigo = int(input("Ingrese el código del empleado " + str(i) + ": "))
    for I in range(1,5):
        # --- Quitar el último dígito
        UD = Codigo % 10
        Codigo = Codigo // 10
        # --- Verificar si D es primo
        if ((UD == 2) or (UD == 3) or (UD == 5) or (UD == 7)):
            NroDigPrimos += 1
    # --- Verificar si tiene NroDigPrimos para ser válido
    if (NroDigPrimos >= 2):
        CodigosValidos += 1
# --- Determinar % de códigos válidos
print(CodigosValidos)
Porcentaje = (CodigosValidos / NroEmp) * 100
# --- Mostrar los resultados (el porcentaje de códigos válidos)
print(f"Porcentaje={Porcentaje}%")
