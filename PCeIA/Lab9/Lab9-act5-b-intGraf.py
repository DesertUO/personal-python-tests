import tkinter as tk
# Función que calcula el número de dígitos impares
def calcular_digitos_impares():
    try:
        # Obtener el número de 3 cifras ingresado por el usuario
        nro = int(entry_nro.get())
        # Validar que el número tiene exactamente 3 cifras
        if nro < 100 or nro > 999:
            etiqueta_resultado.config(text="Debe ingresar un número de exactamente 3 cifras.", fg="red")
            return
        
        # Descomponer el número en sus unidades, decenas y centenas
        unidad = nro % 10
        decena = (nro // 10) % 10
        centena = nro // 100
        
        # Calcular el número de dígitos impares
        digitos_impares = (unidad % 2) + (decena % 2) + (centena % 2)
        
        # Mostrar el resultado dentro de la misma ventana
        etiqueta_resultado.config(text=f"El número de dígitos impares es: {digitos_impares}", fg="black")
    
    except ValueError:
        etiqueta_resultado.config(text="Por favor ingrese un número válido.", fg="red")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Contador de Dígitos Impares")

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="Ingrese un número de 3 cifras:")
etiqueta.pack(pady=10)

# Crear un campo de entrada (Entry)
entry_nro = tk.Entry(ventana, width=15)
entry_nro.pack(pady=5)

# Crear un botón para realizar el cálculo
boton_calcular = tk.Button(ventana, text="Calcular Dígitos Impares", command=calcular_digitos_impares)
boton_calcular.pack(pady=10)

# Crear una etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12))
etiqueta_resultado.pack(pady=20)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
