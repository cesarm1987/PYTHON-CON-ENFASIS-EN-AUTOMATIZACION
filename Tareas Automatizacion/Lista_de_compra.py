cesta = {}
more = 'Si'
while more == 'Si':
    item = input('Introduce un artículo: ')
    price = float(input('Introduce el precio de ' + item + ': '))
    cesta[item] = price
    more = input('¿Quieres añadir artículos a la lista (Si/No)? ')
cost = 0
print('Lista de la compra')
for item, price in cesta.items():
    print(item, '\t', price)
    cost += price
print('Costo total: ', cost)
