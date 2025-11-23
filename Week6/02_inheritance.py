"""
Week 6: Inheritance Examples
Topics: Inheritance, super(), method overriding
"""

class Animal:
    """Base class"""
    
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return "Some sound"
    
    def info(self):
        return f"{self.name} is an animal"


class Dog(Animal):
    """Derived class"""
    
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent constructor
        self.breed = breed
    
    def make_sound(self):  # Override parent method
        return "Woof!"
    
    def info(self):
        return f"{self.name} is a {self.breed} dog"


class Cat(Animal):
    """Another derived class"""
    
    def make_sound(self):
        return "Meow!"


print("=== Inheritance ===")
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")

print(dog.info())
print(f"{dog.name} says: {dog.make_sound()}")
print(f"{cat.name} says: {cat.make_sound()}")
