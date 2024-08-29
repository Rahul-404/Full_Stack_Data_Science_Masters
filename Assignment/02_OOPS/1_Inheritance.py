# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

# Derived class
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age) # Call the constructor of the base
        self.student_id = student_id

    def introduce(self):
        super().introduce() # Calling the introduce method of base class
        print(f"My student ID is {self.student_id}")

# Check in action
obj = Student("Rahul", 25, 65)
obj.introduce()