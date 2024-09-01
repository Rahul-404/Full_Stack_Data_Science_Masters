class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            return StopIteration # Signal that iteration is complete
        
# Create an instance of the iterator
iterable = MyIterator([1, 2, 3])

# Use a try-except block to handle StopIteration
while True:
    try:
        print(next(iterable)) # Attempt to get the next item
    except StopIteration:
        print("End of iteration.")
        break