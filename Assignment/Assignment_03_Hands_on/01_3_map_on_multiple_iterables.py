# Define a function that adds two numbers
def add(x, y):
    return x + y

# Define two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Use map() to apply the add function to pairs of elements from both list
result = map(add, list1, list2)

# Convert the map object to a list and print the result
print(list(result))