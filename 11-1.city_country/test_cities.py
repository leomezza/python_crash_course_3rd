from city_functions import get_formatted_location


def test_city_country():
    """Do locations like 'Santiago, Chile' work?"""
    formatted_location = get_formatted_location("santiago", "chile")
    assert formatted_location == "Santiago, Chile"
