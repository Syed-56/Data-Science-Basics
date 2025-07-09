with open("readFile.txt","r") as file:
    content = file.read()

print(content)

lines = content.splitlines()
print(lines)