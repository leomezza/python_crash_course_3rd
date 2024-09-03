def make_shirt(size="Large", message="I love Python"):
    """Print the size and the message printed on a T-shirt"""
    print(
        f'The T-shirt with the {size} size will have the message "{message}" printed on it.'
    )


make_shirt()
make_shirt("Medium")
make_shirt("Small", "Learning Python")
