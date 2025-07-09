class Animal:
    def speak(self):
        return "Animal"
    
class Cat:
    def speak(self):
        return "Mewo"


def make_sound(animal):
    print(animal.speak())

make_sound(Cat())