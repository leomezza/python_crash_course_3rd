person_1 = {
    "first_name": "Leonardo",
    "last_name": "Mezzanotti",
    "age": "45",
    "city": "Indaiatuba",
}

person_2 = {
    "first_name": "Celeste",
    "last_name": "Mezzanotti",
    "age": "80",
    "city": "São Paulo",
}

person_3 = {
    "first_name": "Michael",
    "last_name": "Jordan",
    "age": "60",
    "city": "Chicago",
}

people = [person_1, person_2, person_3]

for person in people:
    print(f'First Name: {person["first_name"]}')
    print(f'Last Name: {person["last_name"]}')
    print(f'Age: {person["age"]}')
    print(f'Living city: {person["city"]}\n')
