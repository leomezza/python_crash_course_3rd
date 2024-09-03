def city_country(city, country):
    """Returns the preformatted city and country received in the input"""
    city_and_country = f"{city}, {country}"
    return city_and_country.title()


formatted_cc = city_country("Indaiatuba", "Brazil")
print(formatted_cc)

formatted_cc = city_country("Santos", "Brazil")
print(formatted_cc)

formatted_cc = city_country("Austin", "United States of America")
print(formatted_cc)
