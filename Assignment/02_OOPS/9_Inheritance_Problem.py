# Base class
class Device:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}"

# Derived class Phone
class Phone(Device):
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)
        self.screen_size = screen_size

    def display_info(self):
        base_info =  super().display_info()
        return f"{base_info}, Screen Size: {self.screen_size} inches."

# Derived c;ass Tablet
class Tablet(Device):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def display_info(self):
        base_info =  super().display_info()
        return f"{base_info}, Battery Capacity: {self.battery_capacity}"
    
# Example usage
phone = Phone(brand="Samsung", model="Galaxy S23", screen_size=6.4)
tablet = Tablet(brand="Apple", model="iPad Pro", battery_capacity=8600)

print(phone.display_info())
print(tablet.display_info())  



