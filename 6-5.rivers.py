rivers = {
    "nile": "egypt",
    "tietê": "brazil",
    "missisipi": "united states",
}

for river in rivers.keys():
    print(f"The {river.title()} runs through {rivers[river].title()}")

for river in rivers.keys():
    print(f"{river.title()}")

for country in rivers.values():
    print(f"{country.title()}")
