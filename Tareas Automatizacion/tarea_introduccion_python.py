print ("1. Calcular impuesto de renta")
print ("2. Calcular pago de seguro social")
print ("3. Calcular ayuda socio-economica")
print ("4. Calcular ayuda solidaria")
opcion = int(input("Ingrese opcion: "))
if opcion == 0 or opcion > 4:
    print("Opcion no valida");
else:
    salario = int(input("Ingrese salario: "))
    # Opcion 1. Calcular impuesto de renta
    if opcion == 1:
        if salario > 1000:
            print("Impuesto de renta a pagar es=", salario * 0.10)
        else:
            print("No debe pagar impuesto de renta");
    # Opcion 2. Calcular pago de seguro social
    elif opcion == 2:
        if salario <= 500:
            print("Seguro social a pagar es=", salario * 0.20)
        else:
            print("Seguro social a pagar es=", salario * 0.30)
    # Opcion 3. Calcular ayuda socio-economica
    elif opcion == 3:
        if salario >= 300:
            ayuda = int(100)
            print("Su contribucion para ayuda solidaria es: ", ayuda);
        else:
            print("No aplica para ayuda solidaria");
    # Opcion 4. Calcular ayuda solidaria
    elif opcion == 4:
            if salario > 300:
                descuento = int((salario*3)/100)
                print("Descuento para ayuda socio-económica es: ", descuento)
            else:
                print("No aplica para descuento de ayuda socio-económica");
    else:
            print("Opcion no valida");
