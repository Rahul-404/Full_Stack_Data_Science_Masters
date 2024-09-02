# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map() with a lamnbda function to double each number
double_numbers = map(lambda x: x * 2, numbers)

# Convert the map object to a list and print the result
print(list(double_numbers))