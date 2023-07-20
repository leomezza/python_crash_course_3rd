while True:
    age = input('Welcome to the theater, how old are you? ')
    if int(age) < 3:
        print("You're free to come in")
    elif int(age) <= 12:
        print('Your ticket costs $10')
    elif int(age) < 120:
        print('Your ticket costs $15')
    else:
        print('You are too old to be alive, the theater is now yours')
        break
