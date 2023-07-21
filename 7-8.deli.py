sandwich_orders = ['bauru', 'americano', 'misto quente', 'mortadela', 'queijo quente']
finished_sandwiches = []

while sandwich_orders:
    print(f'I made your {sandwich_orders[-1].title()}')
    finished_sandwiches.append(sandwich_orders.pop())

print('\nThe following sandwiches were made:')
for sandwich in finished_sandwiches:
    print(f'\t{sandwich.title()}')
