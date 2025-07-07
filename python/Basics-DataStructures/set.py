#set always store unique elements
list1 = [1, 2, 2, 3, 4, 4]
unique = set(list1)
print(unique)

mySet = set()   #mySet={}   creates dictionary
mySet = {1,2,3,4}
print(mySet)
mySet.add(5)
mySet.update([6,7])  #adds multiple elements
print(mySet)

mySet.remove(3)      # Removes element, raises error if not found
print(mySet)
mySet.discard(10)    # Removes element, does nothing if not found
mySet.pop()          # Removes and returns a random element
print(mySet)

print(2 in mySet)     
print(10 in mySet)
print(len(mySet))
mySet.clear()        # Empties the set
print(mySet)

frozen = frozenset([1, 2, 3])   #cant add remove update
print(frozen)