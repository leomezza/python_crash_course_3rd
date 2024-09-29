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


restaurant = Restaurant("Gendai", "Sushi")
restaurant.describe_restaurant()
restaurant.open_restaurant()
