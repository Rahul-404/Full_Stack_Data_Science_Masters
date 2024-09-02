# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter() with a lambda function to extract even numbers
even_numbers = filter(lambda x: x % 2 ==0, numbers)


# COnvert the filter object to a list and print the result
print(list(even_numbers))