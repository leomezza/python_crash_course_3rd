"""Module with user class"""


class User:
    """A simple attempt to model a user."""

    def __init__(self, first_name, last_name, age, gender):
        """Initialize user name attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        """Describes the user."""
        print(
            f"{self.first_name} {self.last_name} is {self.age} years old and is {self.gender}."
        )

    def greet_user(self):
        """Greets the user."""
        print(f"Hello {self.first_name}, welcome!")
