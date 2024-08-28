class MyIterator:
    def __init__(self, start, end) -> None:
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


# using iterator
my_iter = MyIterator(1, 5)

for value in my_iter:
    print(value)