"""Module with user classes"""


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


class Privileges:
    """A simple attempt to model the privileges of an user."""

    def __init__(self, privileges=["can add post", "can delete post", "can ban user"]):
        """Initialize the privileges's attributes."""
        self.privileges = privileges

    def show_privileges(self):
        """Print the list of privileges."""
        print("This user has the following privileges:")
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    """Represent a special kind of user."""

    def __init__(self, first_name, last_name, age, gender):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an Admin.
        """
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()
