favorite_numbers = {
    "Leo": [8, 13],
    "Manu": [9, 12],
    "Cla": [38, 27],
    "Lu": [39, 27],
    "Celeste": [42, 80],
}

for person, numbers in favorite_numbers.items():
    print(f"\nName: {person}")
    print(f"Favorite numbers:")
    for number in numbers:
        print(f"\t{number}")
