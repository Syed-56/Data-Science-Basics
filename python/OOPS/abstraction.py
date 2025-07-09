class Animal():
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof"

a= Dog()
print(a.make_sound())