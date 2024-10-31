from pathlib import Path

path = Path("guest_book.txt")

names_amount = 1
names = ""

while True:
    name = input(f"Enter the name number {names_amount}, input 'q' to quit: ")
    if name == "q":
        print(names)
        path.write_text(names)
        break

    names_amount += 1
    names += name + "\n"
