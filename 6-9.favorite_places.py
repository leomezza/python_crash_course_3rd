favorite_places = {
    "Leo": ["Indaiatuba", "Austin"],
    "Cla": ["São Paulo", "New York"],
    "Lu": ["Bertioga"],
}

for person, places in favorite_places.items():
    print(f'\nName: {person}')
    print(f'Favorite places:')
    for place in places:
        print(f'\t{place}')
