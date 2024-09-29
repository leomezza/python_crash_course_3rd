class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describes the restaurant."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} type of food.")

    def open_restaurant(self):
        """Opens the restaurant."""
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, customers):
        """Set the number of served customers to the given value."""
        self.number_served = customers

    def increment_number_served(self, new_customers):
        """Add the given amount to the served customers."""
        self.number_served += new_customers


class IceCreamStand(Restaurant):
    """Represent a specific kind of restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to a Ice Cream Stand.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["lemon", "passion fruit", "chocolate"]

    def display_flavors(self):
        """Print the list of flavors."""
        print("This restaurant serves the following flavors:")
        for flavor in self.flavors:
            print(flavor)


restaurant = IceCreamStand("Gendai", "Sushi")
restaurant.display_flavors()
