# Una tienda ofrece el 15% a todas sus compras.
# Escribir un programa que lea la cantidad y el precio unitario del producto.
# Calcular el descuento y el precio final a pagar.

# Leer los datos (la cantidad y el precio unitario de un producto)
cantidadProd = int(input("Ingrese la cantidad del producto: "))
precioUnitario = float(input("Ingrese el precio por unidad del producto: "))
# Calcular el descuento y precio final a pagar
descuento = cantidadProd * precioUnitario * 0.15
precioFinal = cantidadProd * precioUnitario - descuento
# Mostrar los resultado (el descuento y el monto a pagar)
print("Tiene un descuento de", descuento, "y precio final es de", precioFinal)
