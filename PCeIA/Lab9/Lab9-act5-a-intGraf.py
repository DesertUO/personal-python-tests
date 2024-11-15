import tkinter as tk
from tkinter import messagebox
# Función que calcula los dígitos impares
def calcular_impares():
    try:
        # Leer el número ingresado
        Nro = int(entry_numero.get())
        # Verificar que sea un número de 3 cifras
        if Nro < 100 or Nro > 999:
            messagebox.showerror("Error", "Por favor ingrese un número de 3 cifras.")
            return
        # Descomponer el número
        Unidad = Nro % 10
        Decena = (Nro // 10) % 10
        Centena = Nro // 100

        # Calcular el número de dígitos impares
        digitosImpares = (Unidad % 2) + (Decena % 2) + (Centena % 2)
        # Mostrar el resultado
        label_resultado.config(text=f"El número de cifras impares es: {digitosImpares}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un número válido.")

# Crear la ventana principal
root = tk.Tk()
root.title("Contador de Dígitos Impares")
root.geometry("300x200")

# Etiqueta de instrucciones
label_instrucciones = tk.Label(root, text="Ingrese un número de 3 cifras:")
label_instrucciones.pack(pady=10)

# Campo de entrada para el número
entry_numero = tk.Entry(root)
entry_numero.pack(pady=5)

# Botón para calcular los dígitos impares
btn_calcular = tk.Button(root, text="Calcular", command=calcular_impares)
btn_calcular.pack(pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=10)

# Iniciar el loop de la ventana
root.mainloop()
