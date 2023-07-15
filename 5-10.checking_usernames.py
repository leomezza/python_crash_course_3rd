current_users = ["Admin", "Leo", "manu", "clara", "luana"]
print(current_users)
current_users_lower = [x.lower() for x in current_users]  # this is lower() method inside a -list comprehension-
print(current_users_lower)

new_users = ["admin", "leo", "celeste", "fabio", "giullia"]

for username in new_users:
    if username in current_users_lower:
        print(f"Hello {username.title()}, you need to select a different username")
    else:
        print(f"Your username {username} is available")
