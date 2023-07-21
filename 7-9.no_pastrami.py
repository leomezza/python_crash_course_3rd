sandwich_orders = ['bauru', 'pastrami', 'americano', 'misto quente', 'pastrami', 'mortadela', 'queijo quente', 'pastrami']
finished_sandwiches = []

print('Apologies, today we do not have Pastrami\n')

pastrami_removals = 0

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    pastrami_removals += 1

print(f'Removed {pastrami_removals} order(s) of Pastrami\n')

while sandwich_orders:
    print(f'I made your {sandwich_orders[-1].title()}')
    finished_sandwiches.append(sandwich_orders.pop())

print('\nThe following sandwiches were made:')
for sandwich in finished_sandwiches:
    print(f'\t{sandwich.title()}')
