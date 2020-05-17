inscripcion = 1500
promedio = 0
nombre = " "
descuento = 0
total = 0

nombre = input("Ingrese el nombre del estudiante: ")
promedio = input("Ingrese el promedio del estudiante [1-10]: ")

if (int(promedio)>8):
    descuento = inscripcion * 0.20
else:
    descuento = 0

total = inscripcion - descuento

print("Monto a pagar: ")
print(">>> subtotal:",inscripcion)
print(">>> descuento:",descuento)
print(">>> total:",total)
