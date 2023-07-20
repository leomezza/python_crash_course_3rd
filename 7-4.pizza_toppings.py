topping = ''
while topping != 'quit':
    topping = input('What topping would you like? ')
    if topping == 'quit':
        print('Your Pizza will be ready soon!')
    else:
        print(f'Adding {topping} to your Pizza!')
