import multiprocessing

# creating function
def test():
    print("this is my multiprocessing program")

if __name__ == "__main__": # this is process in itself
    m = multiprocessing.Process(target=test)
    print("this is my main program")
    m.start()
    m.join()