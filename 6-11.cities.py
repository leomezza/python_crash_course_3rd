cities = {
    "Indaiatuba": {
        "country": "Brazil",
        "population": "260.000",
        "fact": "Show de bola",
    },
    "Austin": {
        "country": "USA",
        "population": "2.000.000",
        "fact": "Paraíso",
    },
    "Vinhedo": {
        "country": "Brazil",
        "population": "80.000",
        "fact": "Calmo",
    },
}

for city, info in cities.items():
    print(f"\nCity: {city}")
    print(f'\tCountry: {info["country"]}')
    print(f'\tPopulation: {info["population"]}')
    print(f'\tFact: {info["fact"]}')
