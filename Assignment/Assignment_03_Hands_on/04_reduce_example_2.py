from functools import reduce

# Define a binary function that multiplies two numbers
def multiply(x, y):
    return x * y

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use reduce() to apply the multiply function cumulatively
result = reduce(multiply, numbers)

# Print the result
print(result)