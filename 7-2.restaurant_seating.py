dinner_group = input('How many people for dinner? ')

if int(dinner_group) > 8:
    print(f'Apologies, please wait for a free table that can fit {dinner_group} people')
else:
    print(f'Party of {dinner_group}, your table is ready')
