from functools import reduce

# Define a binary function that adds two numbers
def add(x, y):
    return x + y

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use reduce() to apply the add function cumulatively
result = reduce(add, numbers)

# Print the result
print(result)