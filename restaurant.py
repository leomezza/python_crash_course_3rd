"""This is a class in a module"""


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
