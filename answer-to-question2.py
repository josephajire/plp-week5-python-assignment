# Base class representing a generic animal.
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        pass  # Subclasses should override this method


# Dog subclass implementing move()
class Dog(Animal):
    def move(self):
        print(f"{self.name} is Running")


# Bird subclass implementing move()
class Bird(Animal):
    def move(self):
        print(f"{self.name} is Flying")


# Fish subclass implementing move()
class Fish(Animal):
    def move(self):
        print(f"{self.name} is Swimming")


# Function demonstrating polymorphism by calling move()
def demonstrate_movement(animals):
    for animal in animals:
        animal.move()


# List of animal instances with names
animals = [Dog("Dog1"), Bird("Bird1"), Fish("Fish1")]

print("Animals moving:")
demonstrate_movement(animals)

