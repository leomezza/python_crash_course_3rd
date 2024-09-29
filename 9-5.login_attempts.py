class User:
    """A simple attempt to model a user."""

    def __init__(self, first_name, last_name, age, gender):
        """Initialize user name attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        """Describes the user."""
        print(
            f"{self.first_name} {self.last_name} is {self.age} years old and is {self.gender}."
        )

    def greet_user(self):
        """Greets the user."""
        print(f"Hello {self.first_name}, welcome!")

    def increment_login_attempts(self):
        """Add 1 to login attempts value."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Add 1 to login attempts value."""
        self.login_attempts = 0


user1 = User("Leonardo", "Mezzanotti", 46, "Male")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"{user1.first_name} has logged in {user1.login_attempts} times.")

user1.reset_login_attempts()
print(f"{user1.first_name} has logged in {user1.login_attempts} times.")
