# instance attributes
# class attributes

class Dog:
    # class attributes
    species = "Canis familiaris"

    def __init__(self, name, age):
        # instance attributes
        self.name = name
        self.age = age


# create instances of the Dog class
dog1 = Dog("Moti", 5)
dog2 = Dog("Sheru", 3)

# accessing the attributes
print(dog1.name)
print(dog2.name)
print()
print(dog1.age)
print(dog2.age)
print()
# class attribute can be assessed by both instances
print(dog1.species)
print(dog2.species)
print()

# changing class attributes
dog1.species = "dog1"
dog2.species = "dog2"

print(dog1.species)
print(dog2.species)
print()