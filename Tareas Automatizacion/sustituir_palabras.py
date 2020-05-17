x = int(input("Cuantas palabras ingresará?: "))
lista = []
for i in range(x):
  name = input()
  lista += [name]
y = input("que palabra desea reemplazar?")
z = input("Por cual palabra la quiere reemplazar?")
for i in range(len(lista)):
  if y == lista[i]:
    lista[i] = z
print(lista)
