from pathlib import Path


def count_word(word, path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        # Count the approximate number of words in the file:
        num_words = contents.lower().count(word)
        print(f'The file {path} has about {num_words} times the word "{word}".')


path = Path("Frankenstein.txt")
count_word("the", path)
count_word("the ", path)

path = Path("Romeo and Juliet.txt")
count_word("the", path)
count_word("the ", path)
