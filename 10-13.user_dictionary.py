from pathlib import Path
import json


def get_stored_username(path):
    """Get stored user data if available."""
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        return user_dict
    else:
        return None


def get_new_username(path):
    """Prompt for a new user data."""
    username = input("What is your name? ")
    age = input("How old are you? ")
    email = input("What is your e-mail address? ")
    user_dict = {"username": username, "age": age, "email": email}
    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict


def greet_user():
    """Greet the user by available data."""
    path = Path("username.json")
    user_dict = get_stored_username(path)
    if user_dict:
        correct_user = input(
            "Hello " + user_dict["username"] + ", is that you? (y or n) "
        )
        if correct_user == "y":
            print(
                f"Welcome back, {user_dict['username']}, you are {user_dict['age']} years old and your e-mail is {user_dict['email']}!"
            )
        else:
            user_dict = get_new_username(path)
            print(f"We'll remember you when you come back, {user_dict['username']}!")

    else:
        user_dict = get_new_username(path)
        print(f"We'll remember you when you come back, {user_dict['username']}!")


greet_user()
