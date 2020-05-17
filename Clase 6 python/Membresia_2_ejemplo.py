nombre = input("Nombre del cliente: \n")
membresia = int(input("Ingrese el numero de membresia: \n"))
compra = int(input("Ingrese el monto de la compra: \n"))
if membresia >= 300 and membresia <= 399:
    tipo = "Platinum"
    if compra >= 0 and compra <= 200:
        descuento = compra * 0.09
    else:
        descuento = compra * 0.15
elif membresia >= 200 and membresia <= 299:
    tipo = "Gold"
    if compra >= 0 and compra <= 150:
        descuento = compra * 0.03
    else:
        descuento = compra * 0.07
elif membresia >= 100 and membresia <= 199:
    tipo: "Premium"
    if compra >= 0 and compra <= 125:
        descuento = compra * 0.02
    else:
        descuento = compra * 0.05
elif membresia >= 1 and membresia <= 99:
    tipo = "Normal"
    if compra >= 0 and compra <= 100:
        descuento = 0
    else:
        descuento = compra * 0.03

else:
    print("Numero de membresia incorrecto")

salida = "Cliente: " + nombre + "\n" + "Tipo de membresia: " + tipo + "\n" + "Monto total de compra: " + str(compra) + "\n" + "Descuento: " + str(descuento) + "\n" + "Saldo a pagar: " + str(compra-descuento)
print(salida)