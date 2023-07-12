# multiprocessing 
# create and start multiple processors
# data sharing
# prevent race condition
# queues
# process pools

# create and start multiple processes
from multiprocessing import Process, Value, Array, Lock
import os
import time

def square_numbers():
    for i in range(10):
        i * i
        time.sleep(0.1)

def add_100(number, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1

def add_arr_100(arr, lock):
    for j in range(100):
        for i in range(len(arr)):
            time.sleep(0.01)
            with lock:
                arr[i] += 1

def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)

def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1*i)

def cube(number):
    return number * number * number

if __name__ == "__main__":
    processes = []

    # number of CPU's on the machine, usually a good choice for the number of processors
    num_processes = os.cpu_count()
    lock = Lock()

    # create processes and assign a function for each process
    for i in range(num_processes):
        process = Process(target=square_numbers)
        processes.append(process)

    # start all processes
    for process in processes:
        process.start()

    # wait for all processes to finish
    # block the main program until these processes are finished
    for process in processes:
        process.join()

    # like threads, processes don't share the same memory space, so don't have access to global objects
    # so we need special shared memory objects, we can use Value for a single value, and Array for multiple values
    shared_number = Value('i', 0) # i is integer
    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('number at beginging is ', shared_number.value)
    print('array at the beginging is', shared_array[:])

    process_a = Process(target=add_100, args=(shared_number,lock))
    process_b = Process(target=add_100, args=(shared_number,lock))

    process_arr_a = Process(target=add_arr_100, args=(shared_array, lock))
    process_arr_b = Process(target=add_arr_100, args=(shared_array, lock))

    process_a.start()
    process_b.start()
    process_arr_a.start()
    process_arr_b.start()

    process_a.join()
    process_b.join()
    process_arr_a.join()
    process_arr_b.join()

    print('number at the end is', shared_number.value) # there will be race conditions if we don't use the locks
    print('array at the end is', shared_array[:])

    # using a queue (FIFO)
    # used for process safe data exchanges
    from multiprocessing import Queue

    numbers = range(1, 6)
    q = Queue()

    qp1 = Process(target=square, args=(numbers,q))
    qp2 = Process(target=make_negative, args=(numbers,q))

    qp1.start()
    qp2.start()

    qp1.join()
    qp2.join()

    while not q.empty():
        print(q.get())

    # process pool can be used to manage multiple processes
    # it controls a pool of worker processes 
    # it can manage the data for available processes, by splitting data into smaller chunks
    # pool takes care of a lot of things
    from multiprocessing import Pool

    num = range(1000)

    pool = Pool()

    # 4 important methods
    # map, apply, join, close

    # below function will automatically allocate max number of processes
    # creates those processes based on the cores
    # splits the iterable into equal size chunks
    # submits to the function cube which is parallely processed
    result = pool.map(cube, num)
    # if we know only one function to be executed by the pool
    # pool.apply(cube, num[100])

    
    pool.close()

    pool.join()

    print(result)

