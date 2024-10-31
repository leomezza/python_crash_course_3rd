def get_formatted_location(city, country, population=""):
    """Generate a neatly formatted location name."""
    if population:
        location = f"{city}, {country} - Population {population}"
    else:
        location = f"{city}, {country}"
    return location.title()
