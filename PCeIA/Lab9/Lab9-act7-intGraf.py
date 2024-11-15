import tkinter as tk
# Función para calcular el descuento y el precio final
def calcular_descuento():
    try:
        # Obtener la cantidad de productos y el precio unitario desde los campos de entrada
        cantidad_prod = int(entry_cantidad.get())
        precio_unitario = float(entry_precio.get())
        # Calcular el descuento (15%) y el precio final
        descuento = cantidad_prod * precio_unitario * 0.15
        precio_final = cantidad_prod * precio_unitario - descuento
        # Mostrar los resultados en las etiquetas correspondientes
        etiqueta_descuento.config(text=f"Descuento: ${descuento:.2f}", fg="black")
        etiqueta_precio_final.config(text=f"Precio final a pagar: ${precio_final:.2f}", fg="black")
    except ValueError:
        # Si se ingresa un valor no válido (no numérico)
        etiqueta_descuento.config(text="Por favor ingrese valores válidos.", fg="red")
        etiqueta_precio_final.config(text="", fg="black")
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de Descuento y Precio Final")
# Etiquetas y campos de entrada para la cantidad y precio unitario
etiqueta_cantidad = tk.Label(ventana, text="Cantidad de productos:")
etiqueta_cantidad.pack(pady=5)
entry_cantidad = tk.Entry(ventana, width=15)
entry_cantidad.pack(pady=5)

etiqueta_precio = tk.Label(ventana, text="Precio unitario del producto:")
etiqueta_precio.pack(pady=5)
entry_precio = tk.Entry(ventana, width=15)
entry_precio.pack(pady=5)
# Botón para calcular el descuento y precio final
boton_calcular = tk.Button(ventana, text="Calcular Descuento", command=calcular_descuento)
boton_calcular.pack(pady=10)
# Etiquetas para mostrar el descuento y precio final
etiqueta_descuento = tk.Label(ventana, text="", font=("Arial", 12))
etiqueta_descuento.pack(pady=5)
etiqueta_precio_final = tk.Label(ventana, text="", font=("Arial", 12))
etiqueta_precio_final.pack(pady=5)
# Iniciar el bucle principal de la aplicación
ventana.mainloop()
