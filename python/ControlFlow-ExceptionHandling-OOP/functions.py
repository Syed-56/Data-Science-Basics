def greet():    #basic
    print("Hello")

greet() #function calling

def greetWithName(name):    #parameter
    print(f"Hello, {name}!")

greetWithName("Sultan")

def square(x):  #return type
    return x*x

print(square(5))

def add(a,b):   #multiple parameters
    return a+b

sum = add(1,2)
print(sum)

def greetDefault(name="Guest"):
    print(f"Hello, {name}!")

greetDefault()
greetDefault("Ali")

def Student(name,age):
    print(f"{name} is {age} years old")

Student("Sultan",18)
Student(age=21,name="Khizer")   #here you are calling by explicitly mentioning parameter so order 