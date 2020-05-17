# Ejercicio 4 -------------------------
sueldo = input("Ingrese sueldo empleado: ")
if int(sueldo) < 600:
    extra = int(sueldo) * 0.10
    sueldo = int(sueldo) + int(extra)
    print("Sueldo es: ",sueldo);
else:
    extra = int(sueldo) * 0.05
    sueldo = int(sueldo) + int(extra)
    print("Sueldo es: ",sueldo)