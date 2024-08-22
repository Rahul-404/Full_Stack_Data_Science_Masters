import multiprocessing

def producer(q):
    for i in ["rahul", "shelke", "myskills", "ajay", "thakur"]:
        q.put(i) # it will start putting in to queue


def consume(q):
    while True:
        item = q.get() # get data
        if item is None:
            break
        print(item)

if __name__ == "__main__":
    queue =  multiprocessing.Queue()
    m1 = multiprocessing.Process(target=producer, args=(queue, )) # Enqueue operation
    m2 = multiprocessing.Process(target=consume, args=(queue, )) # Dequeue operation
    m1.start()
    m2.start() 
    queue.put("XYZ")
    m1.join()
    m2.join()