import tkinter as tk

# Función para calcular el área del trapecio
def calcular_area():
    baseMayor = int(entry_base_mayor.get())
    baseMenor = int(entry_base_menor.get())
    altura = int(entry_altura.get())
    area = ((baseMayor + baseMenor) * altura) / 2
    label_resultado.config(text=f"El área del trapecio es: {area}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Área de un Trapecio")
ventana.geometry("400x300")

# Etiquetas y entradas
label_base_mayor = tk.Label(ventana, text="Base mayor:")
label_base_mayor.pack()

entry_base_mayor = tk.Entry(ventana)
entry_base_mayor.pack()

label_base_menor = tk.Label(ventana, text="Base menor:")
label_base_menor.pack()

entry_base_menor = tk.Entry(ventana)
entry_base_menor.pack()

label_altura = tk.Label(ventana, text="Altura:")
label_altura.pack()

entry_altura = tk.Entry(ventana)
entry_altura.pack()

# Botón para calcular el área
boton_calcular = tk.Button(ventana, text="Calcular Área", command=calcular_area)
boton_calcular.pack()

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="El área del trapecio es:")
label_resultado.pack()

# Ejecutar la interfaz
ventana.mainloop()
