import multiprocessing.process


def square(index, value):
    """
    it will extract all the value and will take their squares and return those
    """
    value[index] = value[index]**2


if __name__ == "__main__":
    arr = multiprocessing.Array('i', [ 7,654,6,4,65,4,65,54,1,3])
    process = []
    for i in range(10) :
        m = multiprocessing.Process(target=square, args=(i, arr))
        process.append(m)
        m.start()
        
    for m in process:
        m.join()
    print(list(arr))