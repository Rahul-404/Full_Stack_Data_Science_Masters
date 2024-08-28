def my_generator(start, end):
    current = start
    while current <= end:
        yield current
        current += 1

# using the generator 
for number in my_generator(1, 5):
    print(number)