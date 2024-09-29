class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describes the restaurant."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} type of food.")

    def open_restaurant(self):
        """Opens the restaurant."""
        print(f"{self.restaurant_name} is now open!")


restaurant1 = Restaurant("Gendai", "Sushi")
restaurant1.describe_restaurant()

restaurant2 = Restaurant("Indaia", "Barbecue")
restaurant2.describe_restaurant()

restaurant3 = Restaurant("D'Skina", "Burger")
restaurant3.describe_restaurant()
