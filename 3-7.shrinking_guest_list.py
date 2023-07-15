names = ['Manu', 'Cla', 'Lu']

names[0] = 'Celeste'

names.insert(0, 'Fabio')

names.insert(2, 'Giulia')

names.append('Carlos')

print(f'Sorry, bigger table will not be available, only two guest will be invited from the initial list: {names}')

removed_person = names.pop()
print(f'Apologies {removed_person}, I cannot invite you')

removed_person = names.pop()
print(f'Apologies {removed_person}, I cannot invite you')

removed_person = names.pop()
print(f'Apologies {removed_person}, I cannot invite you')

removed_person = names.pop()
print(f'Apologies {removed_person}, I cannot invite you')


print(f'You are still invited to my party: {names[0]}')
print(f'You are still invited to my party: {names[1]}')

del names[0]
del names[0]

print(f'My list should be empty now: {names}')
