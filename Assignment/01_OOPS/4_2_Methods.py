# types of methods
# 1. instance methods
# 2. class methods
# 3. static methods


class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def bark(self):
        return f"{self.name} says woof!"
    
    # instance method
    def birthday(self):
        self.age+=1
        return f"Happy {self.age}th Birthday, {self.name}"
    
    # class method
    @classmethod
    def species_info(cls):
        return f"All dogs belongs to the species {cls.species}."
    
    @staticmethod
    def dog_sound():
        return "Dogs make a variety of sounds."
    

my_dog = Dog("Sheru", 5)

# access instance methods
print(my_dog.bark())

print(my_dog.birthday())

print()


# access class method
print(my_dog.species_info())

print()

# access static method
print(my_dog.dog_sound())