for i in range(5):  #0-4
    print(i, end=" ")   #this doesn't add new line
print() #for new line

for i in range(1,5):    #1-4
    print(i, end=" ")   #this doesn't add new line
print() #for new line

for i in range(1,10,2): #1-10 but every 2nd number
    print(i, end=" ")   #this doesn't add new line
print() #for new line

myList = ["Food","Water","Shelter"]
for item in myList:
    print(item, end=" ")   #this doesn't add new line
print() #for new line

mySet = set([1,2,3])
for index, value in enumerate(sorted(mySet)):
    print("At Index ",index, "Value = " ,value)
print()

for i in range(5):
    if i==3:
        continue
    print(i, end=" ")
print()

for i in range(100):
    if i==10:
        break
    print(i, end=" ")
print()

x=0
while x<5:  #while loop
    print(x, end=" ")
    x+=1