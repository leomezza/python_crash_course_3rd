def make_sandwich(*args):
    """Print the list of items that have been requested in a sandwich."""
    print("Here is the list of items in your sandwich:")
    for item in args:
        print(f"- {item}")


make_sandwich("cheese")
make_sandwich("ham", "green peppers", "extra cheese")
make_sandwich("egg", "red peppers", "ham")
