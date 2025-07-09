class Student:
    def __init__(self,name,age):    #constructor
        self.name = name
        self.age = age
        self.grade = None #uninitialized

    def greet(self):
        print(f"Hi I am {self.name} and Iam {self.age} years old")

    def set_grade(self, grade):
        self.grade = grade

s1 = Student("Sultan",18)
s1.greet()
s1.set_grade(81)