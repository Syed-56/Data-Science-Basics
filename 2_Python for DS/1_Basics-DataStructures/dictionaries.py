dictionary = {} #empty
person = {"name":"Sultan", "Age":18, "isRich":True}
print(person)
print(person["name"])
person["email"] = "sultan@gmail.com"    #inserting
person["Age"] = 21  #updating
print(person)
del person["isRich"]
print(person)

if "name" in person:
    print("Yes, name is a key")

print(len(person))         
print(type(person))

person.clear()  #removes entire list
print(person)

#nested
students = {
    "student1": {"name": "Ali", "age": 18},
    "student2": {"name": "Sara", "age": 19}
}
print(students["student1"]["name"])