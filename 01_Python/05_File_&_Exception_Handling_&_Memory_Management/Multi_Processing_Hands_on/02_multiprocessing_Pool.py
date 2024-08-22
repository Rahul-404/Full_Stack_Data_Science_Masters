import multiprocessing

def square(x):
    return x**2

if __name__ == "__main__":
    with multiprocessing.Pool(processes=5) as pool:
        out = pool.map(square, [3,4,6,5,7,98,7,3,5])
        print(out)