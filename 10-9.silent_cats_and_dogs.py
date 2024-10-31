from pathlib import Path


def print_content(path):
    """Print the contents in a file."""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        print(contents)


path = Path("cats.txt")
print_content(path)
path = Path("dogs.txt")
print_content(path)