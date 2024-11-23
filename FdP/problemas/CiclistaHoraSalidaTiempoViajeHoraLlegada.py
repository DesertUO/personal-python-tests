'''Un ciclista parte de la plaza de armas a las HH horas, MM minutos y SS segundos.
El tiempo que dura el viaje hasta llegar a la Universidad es T segundos.
Escribir un algorítmo que determine la hora de llegada a la Universidad.'''

# --- Obtener datos
print("Se le va a pedir que ingrese la hora de salida en el siguiente formato HH:MM:SS, ingrese cada dato 1 por 1:")
HH1 = int(input("Ingrese la hora de salida (HH): "))
MM1 = int(input("Ingrese los minutos de salida (MM): "))
SS1 = int(input("Ingrese los segundos de salida (SS): "))
print("Ahora ingrese el tiempo de viaje en segundos (T):")
TiempoViaje = int(input("T (s): "))
# --- Convertir datos obtenidos a segundos
HoraSalida = HH1 * 3600 + MM1 * 60 + SS1
SegundosLLegada = HoraSalida + TiempoViaje
# --- Convertir los datos procesados al formato HH:MM:SS
HH2 = (SegundosLLegada // 3600) % 24
MM2 = (SegundosLLegada % 3600) // 60
SS2 = (SegundosLLegada % 60)
# --- Mostrar Resultados
print("Segun la información:")
print("La hora de salida fue a las ", HH1, ":", MM1, ":", SS1, "hrs")
print("El tiempo de viaje en segundos fue de ", TiempoViaje, " segundos")
print("")
print("La hora de llegada viene a ser a las ", HH2, ":", MM2, ":", SS2, "hrs")
