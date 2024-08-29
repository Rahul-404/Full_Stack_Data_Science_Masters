# Base class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        return f"Name: {self.name}, Salary: {self.salary:.2f}"

# Derived class Manager
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary) # Initialize base class attributes
        self.department = department

    def display_info(self):
        base_info =  super().display_info() # Get base class info
        return f"{base_info}, Department: {self.department}"

# Derived class Developer
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary) # Initalize base class attributes
        self.programming_language = programming_language

    def display_info(self):
        base_info =  super().display_info() # Get base class info
        return f"{base_info}, Programming Language: {self.programming_language}"
    

# Example usage
manager = Manager(name="Alice Smith", salary=90000, department="Sales")
developer = Developer(name="Bob Johanson", salary=85000, programming_language="Python")


print(manager.display_info()) 
print(developer.display_info())