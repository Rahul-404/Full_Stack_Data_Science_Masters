# Define a function that checks if a number is even
def is_even(number):
    return number % 2 == 0

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter() to apply the is_even function to each item in the list
even_numbers = filter(is_even, numbers)

# Convert the filter object to a list and print the result
print(list(even_numbers))