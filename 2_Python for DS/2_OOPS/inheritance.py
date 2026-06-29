class Person:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"My name is {self.name}")

class Student(Person):  #inheritance
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll
        #roll is unique attribute of student and name is initialized in parent constructor

    def display(self):
        self.show()
        print(f"Roll# = {self.roll}")

s = Student("Sultan",101)
s.display()