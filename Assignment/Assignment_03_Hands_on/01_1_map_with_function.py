# Define a function that squares a number
def square(x):
    return x * x

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Usa map() to apply the square function to each item in the list
squared_numbers = map(square, numbers)

# Convert the map object to a list and print the result
print(list(squared_numbers))