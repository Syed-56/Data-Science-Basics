lines = ["first\n", "second\n"]
with open("writingReadingLists.txt", "w") as file:
    file.writelines(lines)

with open("writingReadingLists.txt", "r") as file:
    lines = file.readlines()

print(lines)