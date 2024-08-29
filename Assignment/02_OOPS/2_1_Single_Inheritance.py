# Base Class
class Animal:
    def speak(self):
        print("Animal speaks")

# Derived class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Usage
my_dog = Dog()

# Inherited from Animal
my_dog.speak()

# Defined in Dog
my_dog.bark()