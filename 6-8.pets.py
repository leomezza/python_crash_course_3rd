pet_1 = {
    "name": "Dory",
    "kind": "Dog",
    "owner": "Leo",
}

pet_2 = {
    "name": "Cacau",
    "kind": "Dog",
    "owner": "Gu",
}

pet_3 = {
    "name": "Xarope",
    "kind": "Cat",
    "owner": "Celeste",
}

pet_4 = {
    "name": "Chico",
    "kind": "Dog",
    "owner": "Manu",
}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f'Name: {pet["name"]}')
    print(f'Kind of animal: {pet["kind"]}')
    print(f"Owner's name: {pet['owner']}\n")
