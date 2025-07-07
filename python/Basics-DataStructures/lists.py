myList = ["fruits","veggies","meat"]
print(myList[0])
myList.append("Water")
print(myList)
newList = myList.copy()
print(newList)
print(myList.count("fruits"))
del myList[1]
print(myList)
anotherList = ["Nuts", "Sweets"]
myList.extend(anotherList)
print(myList)
myList.insert(0,"Cereal")
print(myList)
myList.pop(3)   #if no value specified, last value removed
print(myList)
myList.remove("fruits")     #if multiple elements of same values, this removes first instance
print(myList)
myList.reverse()
print(myList)

my_list = [1, 2, 3, 4, 5] 
print(my_list[1:4]) 
# Output: [2, 3, 4] (elements from index 1 to 3)
print(my_list[:3]) 
# Output: [1, 2, 3] (elements from the beginning up to index 2) 
print(my_list[2:]) 
# Output: [3, 4, 5] (elements from index 2 to the end) 
print(my_list[::2]) 
# Output: [1, 3, 5] (every second element)
myList.sort()
print(myList)
print(my_list + myList)