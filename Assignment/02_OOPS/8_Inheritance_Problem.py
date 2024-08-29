import math

# Base class
class Shape:
    def __init__(self, colour, border_width):
        self.colour = colour
        self.border_width = border_width

    def display_info(self):
        return f"Colour: {self.colour}, Border Width: {self.border_width}"

# Derived class Rectangle
class Rectangle(Shape):
    def __init__(self, colour, border_width, length, width):
        super().__init__(colour, border_width) # Initalize base class attributes
        self.length = length
        self.width = width

    def display_info(self):
        base_info =  super().display_info()
        return f"{base_info}, Length: {self.length}, Width: {self.width}"

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, colour, border_width, radius):
        super().__init__(colour, border_width) # Initalize base class attributes
        self.radius = radius

    def display_info(self):
        base_info =  super().display_info() # get base class info
        return f"{base_info}, Radius: {self.radius}"
    
    def area(self):
        return math.pi * (self.radius ** 2)
    

# Example usage
rectangle = Rectangle(colour="Blue", border_width=2, length=10, width=5)
circle = Circle(colour="Red", border_width=1, radius=2)

print(rectangle.display_info())
print(f"Area of rectangle: {rectangle.area()}")

print(circle.display_info())
print(f"Area of circle: {circle.area()}")
