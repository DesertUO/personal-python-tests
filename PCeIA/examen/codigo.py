import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

# Función para conectar con la base de datos
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        port="puerto",
        user="root",  # Cambia esto si usas otro usuario
        password="contraseña",  # Cambia esto si tienes contraseña
        database="Colegio"  # Cambia esto al nombre de tu base de datos
    )

# Función para agregar un nuevo estudiante
def agregar_estudiante():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    fecha_nacimiento = entry_fecha_nacimiento.get()
    direccion = entry_direccion.get()
    telefono = entry_telefono.get()
    email = entry_email.get()
    id_clase = entry_id_clase.get()

    if not nombre or not apellido or not fecha_nacimiento:
        messagebox.showerror("Error", "Por favor, complete todos los campos obligatorios.")
        return

    # Si el ID de clase está vacío, lo dejamos como None en lugar de ""
    if id_clase == "":
        id_clase = None
    else:
        id_clase = int(id_clase) if id_clase.isdigit() else None  # Convierte a int si es válido

    try:
        con = conectar_bd()
        cursor = con.cursor()
        query = """INSERT INTO Estudiantes (nombre, apellido, fecha_nacimiento, direccion, telefono, email, id_clase)
                   VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (nombre, apellido, fecha_nacimiento, direccion, telefono, email, id_clase))
        con.commit()
        messagebox.showinfo("Éxito", "Estudiante agregado correctamente.")
        limpiar_campos()
        actualizar_tabla()
    except mysql.connector.Error as err:
        messagebox.showerror("Error de BD", f"Error al agregar el estudiante: {err}")
    finally:
        if con:
            con.close()

# Función para eliminar un estudiante
def eliminar_estudiante():
    id_estudiante = entry_id_estudiante.get()

    if not id_estudiante:
        messagebox.showerror("Error", "Por favor, ingrese el ID del estudiante a eliminar.")
        return

    try:
        con = conectar_bd()
        cursor = con.cursor()
        query = "DELETE FROM Estudiantes WHERE id_estudiante = %s"
        cursor.execute(query, (id_estudiante,))
        con.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Éxito", "Estudiante eliminado correctamente.")
        else:
            messagebox.showwarning("No encontrado", "No se encontró el estudiante con ese ID.")
        limpiar_campos()
        actualizar_tabla()
    except mysql.connector.Error as err:
        messagebox.showerror("Error de BD", f"Error al eliminar el estudiante: {err}")
    finally:
        if con:
            con.close()

# Función para editar un estudiante
def editar_estudiante():
    id_estudiante = entry_id_estudiante.get()
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    fecha_nacimiento = entry_fecha_nacimiento.get()
    direccion = entry_direccion.get()
    telefono = entry_telefono.get()
    email = entry_email.get()
    id_clase = entry_id_clase.get()

    if not id_estudiante:
        messagebox.showerror("Error", "Por favor, ingrese el ID del estudiante a editar.")
        return

    # Si el ID de clase está vacío, lo dejamos como None en lugar de ""
    if id_clase == "":
        id_clase = None
    else:
        id_clase = int(id_clase) if id_clase.isdigit() else None  # Convierte a int si es válido

    try:
        con = conectar_bd()
        cursor = con.cursor()
        query = """UPDATE Estudiantes 
                   SET nombre = %s, apellido = %s, fecha_nacimiento = %s, direccion = %s, telefono = %s, email = %s, id_clase = %s
                   WHERE id_estudiante = %s"""
        cursor.execute(query, (nombre, apellido, fecha_nacimiento, direccion, telefono, email, id_clase, id_estudiante))
        con.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Éxito", "Estudiante editado correctamente.")
        else:
            messagebox.showwarning("No encontrado", "No se encontró el estudiante con ese ID.")
        limpiar_campos()
        actualizar_tabla()
    except mysql.connector.Error as err:
        messagebox.showerror("Error de BD", f"Error al editar el estudiante: {err}")
    finally:
        if con:
            con.close()

# Función para actualizar la tabla de estudiantes
def actualizar_tabla():
    try:
        con = conectar_bd()
        cursor = con.cursor()
        query = "SELECT * FROM Estudiantes"
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in tree.get_children():
            tree.delete(row)

        for row in rows:
            tree.insert("", tk.END, values=row)

    except mysql.connector.Error as err:
        messagebox.showerror("Error de BD", f"Error al visualizar los estudiantes: {err}")
    finally:
        if con:
            con.close()

# Función para limpiar los campos
def limpiar_campos():
    entry_id_estudiante.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_fecha_nacimiento.delete(0, tk.END)
    entry_direccion.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_id_clase.delete(0, tk.END)

# Función para cargar los datos del estudiante al hacer clic en la tabla
def on_tree_select(event):
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        datos_estudiante = item["values"]
        entry_id_estudiante.delete(0, tk.END)
        entry_id_estudiante.insert(0, datos_estudiante[0])
        entry_nombre.delete(0, tk.END)
        entry_nombre.insert(0, datos_estudiante[1])
        entry_apellido.delete(0, tk.END)
        entry_apellido.insert(0, datos_estudiante[2])
        entry_fecha_nacimiento.delete(0, tk.END)
        entry_fecha_nacimiento.insert(0, datos_estudiante[3])
        entry_direccion.delete(0, tk.END)
        entry_direccion.insert(0, datos_estudiante[4])
        entry_telefono.delete(0, tk.END)
        entry_telefono.insert(0, datos_estudiante[5])
        entry_email.delete(0, tk.END)
        entry_email.insert(0, datos_estudiante[6])
        
        # Si el ID de clase es NULL, mostrar vacío en el campo
        if datos_estudiante[7] is None:
            entry_id_clase.delete(0, tk.END)  # Dejar vacío
        else:
            entry_id_clase.delete(0, tk.END)
            entry_id_clase.insert(0, datos_estudiante[7])

# Crear la ventana principal
root = tk.Tk()
root.title("Formulario de Estudiantes")

# Etiquetas y campos de entrada
tk.Label(root, text="ID Estudiante").grid(row=0, column=0, padx=10, pady=5)
entry_id_estudiante = tk.Entry(root)
entry_id_estudiante.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Nombre").grid(row=1, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Apellido").grid(row=2, column=0, padx=10, pady=5)
entry_apellido = tk.Entry(root)
entry_apellido.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Fecha de Nacimiento").grid(row=3, column=0, padx=10, pady=5)
entry_fecha_nacimiento = tk.Entry(root)
entry_fecha_nacimiento.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Dirección").grid(row=4, column=0, padx=10, pady=5)
entry_direccion = tk.Entry(root)
entry_direccion.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Teléfono").grid(row=5, column=0, padx=10, pady=5)
entry_telefono = tk.Entry(root)
entry_telefono.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Email").grid(row=6, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=6, column=1, padx=10, pady=5)

tk.Label(root, text="ID Clase").grid(row=7, column=0, padx=10, pady=5)
entry_id_clase = tk.Entry(root)
entry_id_clase.grid(row=7, column=1, padx=10, pady=5)

# Botones para las operaciones CRUD
btn_agregar = tk.Button(root, text="Agregar Estudiante", command=agregar_estudiante)
btn_agregar.grid(row=8, column=0, columnspan=2, pady=10)

btn_eliminar = tk.Button(root, text="Eliminar Estudiante", command=eliminar_estudiante)
btn_eliminar.grid(row=9, column=0, columnspan=2, pady=10)

btn_editar = tk.Button(root, text="Editar Estudiante", command=editar_estudiante)
btn_editar.grid(row=10, column=0, columnspan=2, pady=10)

# Árbol de visualización (Treeview)
tree = ttk.Treeview(root, columns=("ID", "Nombre", "Apellido", "Fecha Nac.", "Dirección", "Teléfono", "Email", "ID Clase"), show="headings")
tree.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

# Configuración de las columnas del Treeview
tree.heading("ID", text="ID Estudiante")
tree.heading("Nombre", text="Nombre")
tree.heading("Apellido", text="Apellido")
tree.heading("Fecha Nac.", text="Fecha Nacimiento")
tree.heading("Dirección", text="Dirección")
tree.heading("Teléfono", text="Teléfono")
tree.heading("Email", text="Email")
tree.heading("ID Clase", text="ID Clase")

# Ajustar el tamaño de las columnas
tree.column("ID", width=50, anchor="center")
tree.column("Nombre", width=150)
tree.column("Apellido", width=150)
tree.column("Fecha Nac.", width=100, anchor="center")
tree.column("Dirección", width=200)
tree.column("Teléfono", width=100)
tree.column("Email", width=150)
tree.column("ID Clase", width=80)

# Configurar el evento de selección en el Treeview
tree.bind("<<TreeviewSelect>>", on_tree_select)

# Cargar la tabla de estudiantes al iniciar
actualizar_tabla()

# Iniciar la ventana principal de la interfaz
root.mainloop()
