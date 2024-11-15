import tkinter as tk
# Función para calcular el promedio de las 3 notas
def calcular_promedio():
    try:
        # Obtener las notas ingresadas por el usuario
        nota1 = float(entry_nota1.get())
        nota2 = float(entry_nota2.get())
        nota3 = float(entry_nota3.get())
        # Calcular el promedio
        promedio = (nota1 + nota2 + nota3) / 3
        # Mostrar el resultado en la etiqueta de resultados
        etiqueta_resultado.config(text=f"El promedio del alumno es: {promedio:.2f}", fg="black")
    
    except ValueError:
        # Si el usuario ingresa un valor no válido
        etiqueta_resultado.config(text="Por favor ingrese notas válidas (números).", fg="red")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo del Promedio del Alumno")

# Crear una etiqueta para la introducción de las notas
etiqueta_instrucciones = tk.Label(ventana, text="Ingrese las tres notas del alumno:")
etiqueta_instrucciones.pack(pady=10)
# Crear etiquetas y campos de entrada para cada nota
etiqueta_nota1 = tk.Label(ventana, text="Primera nota:")
etiqueta_nota1.pack(pady=5)
entry_nota1 = tk.Entry(ventana, width=15)
entry_nota1.pack(pady=5)

etiqueta_nota2 = tk.Label(ventana, text="Segunda nota:")
etiqueta_nota2.pack(pady=5)
entry_nota2 = tk.Entry(ventana, width=15)
entry_nota2.pack(pady=5)

etiqueta_nota3 = tk.Label(ventana, text="Tercera nota:")
etiqueta_nota3.pack(pady=5)
entry_nota3 = tk.Entry(ventana, width=15)
entry_nota3.pack(pady=5)
# Crear un botón para calcular el promedio
boton_calcular = tk.Button(ventana, text="Calcular Promedio", command=calcular_promedio)
boton_calcular.pack(pady=10)
# Crear una etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12))
etiqueta_resultado.pack(pady=20)
# Iniciar el bucle principal de la aplicación
ventana.mainloop()
