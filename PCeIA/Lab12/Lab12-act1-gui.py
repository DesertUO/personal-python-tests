import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Funciones base
def aparicion_del_cinco_while(nro, digito_a_encontrar):
    contador = 0
    while nro > 0:
        digito = nro % 10
        if digito == digito_a_encontrar:
            contador += 1
        nro //= 10
    return contador

def promedio_lab_while(n_estudiantes_pc, n_estudiantes_ti, notas_pc, notas_ti):
    promedio_pc = sum(notas_pc) / n_estudiantes_pc
    promedio_ti = sum(notas_ti) / n_estudiantes_ti
    promedio_total = (sum(notas_pc) + sum(notas_ti)) / (n_estudiantes_pc + n_estudiantes_ti)
    return promedio_total

def cobrar_cuota_while(monto_base, notas):
    total_recaudado = 0
    for nota in notas:
        if nota == 20:
            descuento = 0.5
        elif nota >= 17:
            descuento = 0.3
        else:
            descuento = 0
        total_recaudado += monto_base * (1 - descuento)
    return total_recaudado

def dibujar_triangulo(altura):
    return "\n".join(["*" * i for i in range(1, altura + 1)])

def contar_vocales(texto):
    return sum(1 for c in texto if c.lower() in "aeiou")

def sumar_par_impar(n):
    suma_pares = sum(i for i in range(1, n + 1) if i % 2 == 0)
    suma_impares = sum(i for i in range(1, n + 1) if i % 2 != 0)
    return suma_pares, suma_impares

def fibonacci(nro_term):
    term1, term2 = 0, 1
    serie = []
    for _ in range(nro_term):
        serie.append(term1)
        term1, term2 = term2, term1 + term2
    return serie

# Interfaz gráfica
def actualizar_formulario(*args):
    # Limpiar los widgets existentes en frame_inputs y frame_dynamic
    for widget in frame_inputs.winfo_children():
        widget.destroy()
    for widget in frame_dynamic.winfo_children():
        widget.destroy()

    seleccion = combo_funcion.get()

    if seleccion == "Aparición del Dígito (While Loop)":
        tk.Label(frame_inputs, text="Número:").grid(row=0, column=0)
        tk.Entry(frame_inputs, textvariable=var_numero).grid(row=0, column=1)

        tk.Label(frame_inputs, text="Dígito a encontrar:").grid(row=1, column=0)
        tk.Entry(frame_inputs, textvariable=var_digito).grid(row=1, column=1)

    elif seleccion == "Promedio Laboratorio":
        tk.Label(frame_inputs, text="Estudiantes PC:").grid(row=0, column=0)
        tk.Entry(frame_inputs, textvariable=var_estudiantes_pc).grid(row=0, column=1)

        tk.Label(frame_inputs, text="Estudiantes TI:").grid(row=1, column=0)
        tk.Entry(frame_inputs, textvariable=var_estudiantes_ti).grid(row=1, column=1)

        # Crear botón para generar entradas dinámicas
        tk.Button(frame_inputs, text="Generar Entradas de Notas", command=generar_entradas_notas).grid(row=2, column=0, columnspan=2)

    elif seleccion == "Cobrar Cuota":
        tk.Label(frame_inputs, text="Monto base:").grid(row=0, column=0)
        tk.Entry(frame_inputs, textvariable=var_monto_base).grid(row=0, column=1)

        tk.Label(frame_inputs, text="Cantidad de compañeros:").grid(row=1, column=0)
        tk.Entry(frame_inputs, textvariable=var_cantidad_companeros).grid(row=1, column=1)

        # Crear botón para generar entradas dinámicas
        tk.Button(frame_inputs, text="Generar Entradas de Notas", command=generar_entradas_notas).grid(row=2, column=0, columnspan=2)

    elif seleccion == "Dibujar Triángulo":
        tk.Label(frame_inputs, text="Altura del triángulo:").grid(row=0, column=0)
        tk.Entry(frame_inputs, textvariable=var_altura).grid(row=0, column=1)

    elif seleccion == "Contar Vocales":
        tk.Label(frame_inputs, text="Texto:").grid(row=0, column=0)
        tk.Entry(frame_inputs, textvariable=var_texto).grid(row=0, column=1)

    elif seleccion == "Sumar Pares e Impares":
        tk.Label(frame_inputs, text="Número límite:").grid(row=0, column=0)
        tk.Entry(frame_inputs, textvariable=var_limite).grid(row=0, column=1)

    elif seleccion == "Serie Fibonacci":
        tk.Label(frame_inputs, text="Términos a imprimir:").grid(row=0, column=0)
        tk.Entry(frame_inputs, textvariable=var_terminos).grid(row=0, column=1)

    canvas.after(100, actualizar_scrollregion)

def generar_entradas_notas():
    for widget in frame_dynamic.winfo_children():
        widget.destroy()

    seleccion = combo_funcion.get()
    if seleccion == "Promedio Laboratorio":
        cantidad_pc = var_estudiantes_pc.get()
        cantidad_ti = var_estudiantes_ti.get()

        # Limpiar las listas de notas de los laboratorios
        global var_notas_pc, var_notas_ti
        var_notas_pc = [tk.IntVar() for _ in range(cantidad_pc)]
        var_notas_ti = [tk.IntVar() for _ in range(cantidad_ti)]

        # Nueva etiqueta de comentario para aumentar el tamaño de la ventana
        tk.Label(frame_dynamic, text="Aumenta el tamaño de la ventana para ver las notas CASI correctamente.\nTal vez en pantalla completa.").grid(row=0, column=0, columnspan=2)
        tk.Label(frame_dynamic, text="Notas PC:").grid(row=1, column=0)
        for i in range(cantidad_pc):
            tk.Label(frame_dynamic, text=f"Nota {i + 1}:").grid(row=i + 2, column=0)  # Etiqueta de numeración
            tk.Entry(frame_dynamic, textvariable=var_notas_pc[i]).grid(row=i + 2, column=1)

        tk.Label(frame_dynamic, text="Notas TI:").grid(row=0, column=1)
        for i in range(cantidad_ti):
            tk.Label(frame_dynamic, text=f"Nota {i + 1}:").grid(row=i + 2, column=1)  # Etiqueta de numeración
            tk.Entry(frame_dynamic, textvariable=var_notas_ti[i]).grid(row=i + 2, column=2)



def actualizar_scrollregion(event):
    # Actualiza el 'scrollregion' solo cuando sea necesario
    canvas.config(scrollregion=canvas.bbox("all"))

def ejecutar_funcion():
    seleccion = combo_funcion.get()

    if seleccion == "Aparición del Dígito (While Loop)":
        numero = var_numero.get()
        digito = var_digito.get()
        resultado = aparicion_del_cinco_while(numero, digito)
        resultado_label.config(text=f"Resultado: El dígito aparece {resultado} veces.")

    elif seleccion == "Promedio Laboratorio":
        estudiantes_pc = var_estudiantes_pc.get()
        estudiantes_ti = var_estudiantes_ti.get()
        notas_pc = [var.get() for var in var_notas_pc]
        notas_ti = [var.get() for var in var_notas_ti]
        resultado = promedio_lab_while(estudiantes_pc, estudiantes_ti, notas_pc, notas_ti)
        resultado_label.config(text=f"Resultado: El promedio general es {resultado:.2f}.")

    elif seleccion == "Cobrar Cuota":
        monto_base = var_monto_base.get()
        notas = [var.get() for var in var_notas_companeros]
        resultado = cobrar_cuota_while(monto_base, notas)
        resultado_label.config(text=f"Resultado: Total recaudado: S/.{resultado:.2f}")

    elif seleccion == "Dibujar Triángulo":
        altura = var_altura.get()
        resultado = dibujar_triangulo(altura)

        # Mostrar el triángulo en el widget Text
        resultado_texto.config(state=tk.NORMAL)  # Habilitar edición temporalmente
        resultado_texto.delete("1.0", tk.END)  # Limpiar el contenido previo
        resultado_texto.insert(tk.END, resultado)  # Insertar el texto procesado
        resultado_texto.config(state=tk.DISABLED)  # Deshabilitar para que sea de solo lectura

    elif seleccion == "Contar Vocales":
        texto = var_texto.get()
        resultado = contar_vocales(texto)
        resultado_label.config(text=f"Resultado: El texto contiene {resultado} vocales.")

    elif seleccion == "Sumar Pares e Impares":
        limite = var_limite.get()
        suma_pares, suma_impares = sumar_par_impar(limite)
        resultado_label.config(
            text=f"Resultado:\nSuma de pares: {suma_pares}\nSuma de impares: {suma_impares}"
        )

    elif seleccion == "Serie Fibonacci":
        terminos = var_terminos.get()
        resultado = fibonacci(terminos)
        resultado_label.config(text=f"Resultado: Serie Fibonacci: {', '.join(map(str, resultado))}")

# Ventana principal
root = tk.Tk()
root.title("Funciones Dinámicas")

# Variables
var_numero = tk.IntVar()
var_digito = tk.IntVar()
var_estudiantes_pc = tk.IntVar()
var_estudiantes_ti = tk.IntVar()
var_monto_base = tk.IntVar()
var_cantidad_companeros = tk.IntVar()
var_altura = tk.IntVar()
var_texto = tk.StringVar()
var_limite = tk.IntVar()
var_terminos = tk.IntVar()

var_notas_pc = [tk.IntVar() for _ in range(100)]
var_notas_ti = [tk.IntVar() for _ in range(100)]
var_notas_companeros = [tk.IntVar() for _ in range(100)]

# Layout
frame_controls = tk.Frame(root)
frame_controls.pack(pady=10)

frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

# Crear un canvas con un scrollbar para el frame_dynamic
canvas = tk.Canvas(root, height=400)  # Aumenta el valor de 'height' según lo necesario
canvas.pack(pady=10, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

frame_dynamic = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame_dynamic, anchor="nw")
canvas.config(yscrollcommand=scrollbar.set)

frame_dynamic.bind("<Configure>", actualizar_scrollregion)

frame_result = tk.Frame(root)
frame_result.pack(pady=10)

# Widgets principales
tk.Label(frame_controls, text="Seleccione una función:").grid(row=0, column=0)
combo_funcion = ttk.Combobox(frame_controls, state="readonly")
combo_funcion["values"] = [
    "Aparición del Dígito (While Loop)",
    "Promedio Laboratorio",
    "Cobrar Cuota",
    "Dibujar Triángulo",
    "Contar Vocales",
    "Sumar Pares e Impares",
    "Serie Fibonacci",
]
combo_funcion.grid(row=0, column=1)
combo_funcion.bind("<<ComboboxSelected>>", actualizar_formulario)

tk.Button(frame_controls, text="Ejecutar", command=ejecutar_funcion).grid(row=0, column=2)

# Etiqueta de resultado
resultado_label = tk.Label(frame_result, text="Resultado:")
resultado_label.pack()

resultado_texto = tk.Text(frame_result, height=10, width=50, wrap=tk.WORD)
resultado_texto.pack(pady=5)
resultado_texto.config(state=tk.DISABLED)  # Para que inicialmente sea de solo lectura

# Iniciar aplicación
root.mainloop()