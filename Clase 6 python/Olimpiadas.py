nombre = input("Nombre del Atleta: \n")
print("Escoger evento")
print("1. 100mts Plano")
print("2. 400mts obstaculos")
print("3. 1500mts planos")
print("4. 3000mts planos")
opcion = int(input("Ingresar Opcion: \n"))
if opcion == 1:
    tiempo = int(input("Dame el tiempo en segundos: \n"))
    if tiempo > 20:
        print(nombre, ", 100mts Plano" ,"No clasifica a ningun evento")
    elif tiempo > 15:
        print(nombre, ", 100mts Plano", "Clasifica a juegos nacionales")
    else:
        print(nombre, ", 100mts Plano", "Clasifica a juegos olimpicos")
elif opcion == 2:
    tiempo = int(input("Dame el tiempo en segundos: \n"))

    if tiempo > 75:
        print(nombre, ", 100mts Obstaculos", "No clasifica a ningun evento")
    elif tiempo > 60:
        print(nombre, ", 100mts Obstaculos", "Clasifica a juegos nacionales")
    else:
        print(nombre, ", 100mts Plano", "Clasifica a juegos olimpicos")


elif opcion == 3:
    tiempo = float(input("Dame el tiempo en minutos: \n"))
    if tiempo > 3.0:
        print(nombre, ", 1500mts Plano", "No clasifica a ningun evento")
    elif tiempo > 3.5:
        print(nombre, ", 1500mts Plano", "Clasifica a juegos nacionales")
    else:
        print(nombre, ", 1500mts Plano", "Clasifica a juegos olimpicos")

elif opcion == 4:
    tiempo = float(input("Dame el tiempo en minutos: \n"))
    if tiempo > 7.0:
        print(nombre, ", 3000mts Plano", "No clasifica a ningun evento")
    elif tiempo > 6.0:
        print(nombre, ", 3000mts Plano", "Clasifica a juegos nacionales")
    else:
        print(nombre, ", 3000mts Plano", "Clasifica a juegos olimpicos")

else:
    print("Opcion Invalida")