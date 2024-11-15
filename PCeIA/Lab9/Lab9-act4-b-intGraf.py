import tkinter as tk
# Función para calcular la distancia entre dos puntos
def calcular_distancia():
    # Obtener los valores de las entradas
    x1 = float(entry_x1.get())
    y1 = float(entry_y1.get())
    x2 = float(entry_x2.get())
    y2 = float(entry_y2.get())
    
    # Calcular la distancia
    distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    # Mostrar el resultado en la etiqueta
    label_resultado.config(text=f"La distancia es: {distancia:.2f}")
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Distancia entre dos puntos")
ventana.geometry("400x300")
# Etiquetas y campos de entrada
label_x1 = tk.Label(ventana, text="Coordenada x del punto 1:")
label_x1.pack()

entry_x1 = tk.Entry(ventana)
entry_x1.pack()

label_y1 = tk.Label(ventana, text="Coordenada y del punto 1:")
label_y1.pack()

entry_y1 = tk.Entry(ventana)
entry_y1.pack()

label_x2 = tk.Label(ventana, text="Coordenada x del punto 2:")
label_x2.pack()

entry_x2 = tk.Entry(ventana)
entry_x2.pack()

label_y2 = tk.Label(ventana, text="Coordenada y del punto 2:")
label_y2.pack()

entry_y2 = tk.Entry(ventana)
entry_y2.pack()
# Botón para calcular la distancia
boton_calcular = tk.Button(ventana, text="Calcular Distancia", command=calcular_distancia)
boton_calcular.pack(pady=10)
# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="La distancia es:")
label_resultado.pack()
# Ejecutar la interfaz
ventana.mainloop()
