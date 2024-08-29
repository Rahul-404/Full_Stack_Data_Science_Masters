# Base class
class Vahicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"
    
    def start_engine(self):
        return f"The engine of the {self.display_info()} is starting."
    

# Derived class
class Car(Vahicle):
    def __init__(self, make, model, year, fule_type):
        super().__init__(make, model, year) # Call the constructor of the base class
        self.fule_type = fule_type

    def display_info(self):
        # Override the base class method to include fule type
        base_info =  super().display_info()
        return f"{base_info}, Fule Type: {self.fule_type}"
    
    def start_engine(self):
        # Optionally, override the base class methof if needed
        return f"The {self.fule_type} engine of the {self.display_info()}"
    
# Example usage
my_car = Car(make="TATA", model="Mahindra", year=2024, fule_type="Hydrogen")

print(my_car.display_info())
print(my_car.start_engine())