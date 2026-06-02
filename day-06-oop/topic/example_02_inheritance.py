"""Example 2: Inheritance Hierarchy

Animal -> Mammal -> Dog/Cat
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement speak()")

class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

    def warm_blooded(self):
        return True

class Dog(Mammal):
    def __init__(self, name, fur_color, breed):
        super().__init__(name, fur_color)
        self.breed = breed

    def speak(self):
        return f"{self.name} says woof!"

class Cat(Mammal):
    def speak(self):
        return f"{self.name} says meow!"


animals = [
    Dog("Rex", "brown", "Labrador"),
    Cat("Whiskers", "gray"),
]

for a in animals:
    print(f"{a.name}: {a.speak()}")
    if isinstance(a, Dog):
        print(f"  Breed: {a.breed}")
