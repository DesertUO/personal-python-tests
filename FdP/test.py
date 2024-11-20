'''La granja "La Liebre" vende liebres a S/. X cada liebre.
Escribir un algorítmo que lea el número de liebres vendidas y el costo unitario; luego que determine: el valor de la venta, el impuesto a pagar (IGV = 18%) y el importe total.'''

# --- Leer el Nro. Unidades y Costo Unitario
NroUnidades = float(input("Ingresar el Nro. de Unidades: "))
CostoUnitario = float(input("Ingresar el Costo Unitario: "))
# --- Calcular Valor Venta, Impuesto y Importe Total
ValorVenta = NroUnidades * CostoUnitario
Impuesto = ValorVenta * 0.18
ImporteTotal = ValorVenta + Impuesto
# --- Mostrar Resultados
print("El valor venta = ", ValorVenta, ", el impuesto = ", Impuesto, " y el importe total =  ", ImporteTotal, ".")
