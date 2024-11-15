import tkinter as tk
# Función para calcular el número de dígitos pares
def calcular_digitos_pares():
    try:
        # Obtener el número de 4 cifras ingresado por el usuario
        nro = int(entry_nro.get())
        # Validar que el número tenga exactamente 4 cifras
        if nro < 1000 or nro > 9999:
            etiqueta_resultado.config(text="Debe ingresar un número de 4 cifras.", fg="red")
            return
        # Descomponer el número en unidades, decenas, centenas y millares
        unidad = nro % 10
        decena = (nro // 10) % 10
        centena = (nro // 100) % 10
        millar = nro // 1000
        # Determinar el número de cifras pares
        cifras_pares = ((unidad + 1) % 2) + ((decena + 1) % 2) + ((centena + 1) % 2) + ((millar + 1) % 2)
        # Mostrar los resultados en la etiqueta
        etiqueta_resultado.config(text=f"El número de cifras pares es: {cifras_pares}", fg="black")
    
    except ValueError:
        etiqueta_resultado.config(text="Por favor ingrese un número válido de 4 cifras.", fg="red")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Contador de Dígitos Pares")
ventana.geometry("300x250")  # Añadir tamaño fijo para la ventana

# Crear una etiqueta de instrucciones
etiqueta = tk.Label(ventana, text="Ingrese un número de 4 cifras:", font=("Arial", 12))
etiqueta.pack(pady=15)

# Crear un campo de entrada (Entry) para el número
entry_nro = tk.Entry(ventana, width=20, font=("Arial", 12))
entry_nro.pack(pady=5)

# Crear un botón para calcular el número de dígitos pares
boton_calcular = tk.Button(ventana, text="Calcular Dígitos Pares", command=calcular_digitos_pares, font=("Arial", 12))
boton_calcular.pack(pady=10)

# Crear una etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12))
etiqueta_resultado.pack(pady=20)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
