import multiprocessing

def sender(conn, msg):
    ''' 
    this will send a message after establishing a connection, a pipe will create this connection
    '''
    for i in msg:
        conn.send(i)
    conn.close()

def receive(conn):
    while True:
        try:
            msg = conn.recv()
        except Exception as e:
            print(e)
            break
        print(msg)


if __name__ == "__main__":
    msg = ["my name is rahul", "this is my msg to my students", "i am taking class for dsm ", "try to practice all the code"]
    # establish the connection using pipe
    parent_conn, child_conn = multiprocessing.Pipe() 
    # by default duplex connection will be formed, besically everyone can send and every one can recive
    # if duplex = false then messeging will happen in simplex mode, means one can only send and one can only receive 
    m1 = multiprocessing.Process(target=sender, args=(child_conn, msg))
    m2 = multiprocessing.Process(target=receive, args=(parent_conn,))
    m1.start()
    m2.start()
    m1.join()
    child_conn.close()
    m2.join()
    parent_conn.close()