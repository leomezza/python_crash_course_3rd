from pathlib import Path

path = Path("pi_digits.txt")
contents = path.read_text()

print(contents.splitlines())

for line in contents.splitlines():
    print(line)
