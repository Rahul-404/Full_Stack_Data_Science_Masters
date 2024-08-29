# Base class (super class)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Derived class (subclass)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) # call the constructor of the base class
        self.breed = breed

    def speak(self):
        super().speak() # Call the speak method of the base class
        print(f"{self.name} barks")

# Usage
my_dog = Dog(name="Buddy", breed="Golden Retriever")
my_dog.speak()