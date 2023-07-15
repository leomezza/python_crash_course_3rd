favorite_pizzas = ['dois queijos', 'portuguesa', 'abobrinha']

friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append('mussarela')

friend_pizzas.append('peperoni')

print('My favorite pizzas are:')
for pizza in favorite_pizzas:
    print(pizza.title())

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())
