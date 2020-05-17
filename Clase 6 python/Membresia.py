nombre_cliente = str(input("Ingrese el nombre del cliente: "))
membresia = int(input("Ingrese su numero de membresia "))
monto_compra = float(input("Indique el monto total de la compra "))
tipo_membresia = str("")
descuento = float (0)
saldo_pagar = float (0)

if membresia >= 0 and membresia <= 99:
    tipo_membresia = "NORMAL"
    if monto_compra > 0 and monto_compra < 100:
        descuento = 0
        saldo_pagar = monto_compra
    else:
        descuento = monto_compra * 0.03
        saldo_pagar = monto_compra - descuento
elif membresia >= 100 and membresia <= 199:
    tipo_membresia = "PREMIUM"
    if monto_compra > 0 and monto_compra < 125:
        descuento = monto_compra * 0.02
        saldo_pagar = monto_compra - descuento
    else:
        descuento = monto_compra * 0.05
        saldo_pagar = monto_compra - descuento
elif membresia >= 200 and membresia <= 299:
    tipo_membresia = "GOLD"
    if monto_compra > 0 and monto_compra < 150:
        descuento = monto_compra * 0.03
        saldo_pagar = monto_compra - descuento
    else:
        descuento = monto_compra * 0.07
        saldo_pagar = monto_compra - descuento
elif membresia >= 300 and membresia <= 399:
    tipo_membresia = "PLATINUM"
    if monto_compra > 0 and monto_compra < 200:
        descuento = monto_compra * 0.09
        saldo_pagar = monto_compra - descuento
    else:
        descuento = monto_compra * 0.15
        saldo_pagar = monto_compra - descuento

else:
    print("Numero de membresia no valido")

print("\n\n\nCliente: ", nombre_cliente, "\nNumero de membresia: ", membresia, "\nTipo de membresia: ", tipo_membresia, "n\Monto Total de la compra: ",monto_compra,"\nDescuento: ",descuento, "\nSaldo a pagar: ",saldo_pagar)