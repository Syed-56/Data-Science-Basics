f= open("readFile.txt","r")
content = f.read()
print(content)

f.seek(0)   #reset cursor to beginning
lines = []  #store file contents organizingly
while True:
    line = f.readline()
    if not line:
        break
    lines.append(line.strip())  #strip removes newline character

print(lines)
f.close()