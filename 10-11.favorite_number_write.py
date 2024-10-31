from pathlib import Path
import json

fav_number = input("What is your favorite number? ")

path = Path("fav_number.json")
contents = json.dumps(fav_number)
path.write_text(contents)

print(f"We'll remember your favorite number {fav_number}!")
