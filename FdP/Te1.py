# Programa ejemplo de modularidad

# Módulo que muestra una línea de asteriscos
def Asteriscos(text):
    print("*"*(len(text)+2))

def EncerrarTexto(text):
    print("*"*(len(text)+2))
    print("*"+text+"*")
    print("*"*(len(text)+2))

# Mostrar mensajes con líneas de asteriscos
U1 = "UNSAAC"
U2 = "Ingeniería Informática y de Sistemas"
U3 = "CUSCO - PERÚ"
EncerrarTexto(U1)
EncerrarTexto(U2)
EncerrarTexto(U3)
