from pathlib import Path

path = Path("learning_python.txt")
contents_python = path.read_text()
print(contents_python)

contents = contents_python.replace("Python", "C")
print(contents)

lines = contents.splitlines()
print(lines)
for line in lines:
    print(line)
