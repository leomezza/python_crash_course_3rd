from pathlib import Path
import json

path = Path("fav_number.json")

if path.exists():
    contents = path.read_text()
    fav_number = json.loads(contents)
    print(f"I know your favorite number! It’s {fav_number}!")
else:
    fav_number = input("What is your favorite number? ")
    contents = json.dumps(fav_number)
    path.write_text(contents)
    print(f"We'll remember your favorite number {fav_number}!")
