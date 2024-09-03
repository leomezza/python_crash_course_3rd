def describe_city(city, country="Brazil"):
    """Print the name of the city and its country"""
    print(
        f'{city} is in {country}.'
    )


describe_city("Indaiatuba")
describe_city("Santos")
describe_city("Austin", "United States of America")
