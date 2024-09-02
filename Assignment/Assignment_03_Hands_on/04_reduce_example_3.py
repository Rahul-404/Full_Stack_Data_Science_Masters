from functools import reduce

# Define a binary function that adds two numbers
def add(x, y):
    return x + y

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# use reduce() with an initalizer (initial value)
result = reduce(add, numbers, 10)

# Print the result
print(result)