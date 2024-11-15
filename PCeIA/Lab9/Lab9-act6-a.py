# Escribir un algoritmo que evalúe la función: f(x)= 2x^2+ 3x-5

# Leer los datos (el valor de x)
print("f(x) = 2x^2 + 3x + 5")
X = int(input("Ingrese el valor de x para evaluar la función f(x) (X): "))
# Evaluar la funcion f(x) en x = X
fDeX = 2 * (X ** 2) + 3 * X + 5
# Mostrar los resultados (la función evaluada en x = X)
print("El valor de f(x) para x", X, " es", fDeX)
