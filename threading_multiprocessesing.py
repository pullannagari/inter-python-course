# run code in parallel and speed up the code
# diff b/w threads and process
# advantanges and disadvantages of both
# limitation of threads by GIL
# built in threads and multiprocessing module

# diff b/w thread and process

    # a process is an instance of a program
    # one python interpreter, firefox browser example
    # process can have multiple threads
    # processes take advantage of multiple cpu's and core
    # process have a separate memory space, not shared b/w processes
    # processes are great for cpu bound processing
    # for ex. if we have a large amount of data and need to perform expensive computation, we can use multiprocessing to process within each cpu in parallel
    # a new process is started independently from other processes
    # processes are easily interruptable and killable
    # there is one GIL for each process - avoids GIL limitation
    # process is heavy weight
    # starting a process is slower than starting the thread
    # interprocess communication is complex since the memory space is not shared

    # thread is an entitiy within a process that can be scheduled for execution
    # also known as light-weight process
    # a process can spawn multiple threads, share the same memory, lightweight, starting a thread is fast than starting a process
    # great for IO bound tasks 
    # for ex. when the program has to talk to slow devices such as hard drive or network call. with threading your program can use the time waiting for these devices to switch to other threads to do some processing
    # threading is limited by the GIL
    # GIL allows only one thread at a time
    # threading has no effect for CPU bound tasks
    # threads are not interruptable or killable, need to be careful with memory leaks
    # since threads share the same memory space we need to be careful of the race conditions

# GIL - global interpretter lock
# its a lock in python which allows only one thread to be executed at a time
# controversial in the python community
# this is needed in cpython which is the reference implementation of python, when installled python
# cpython there is technique that is called reference counting used for memory management. this is used to count the number of references to the same object to be able to check and garbage collect.
# if this counting is not thread safe there is a chance of garbage collecting the active objects, or causing memory leaks by not able to garbage collect due to race conditions.
# a couple of ways to avoid GIL - multiprocessing, use different free threaded python implementation jython or ironpython or use python as a wrapper for 3rd party libraries

# multiprocessing

from multiprocessing import Process
import os
import time

def square_numbers():
        for i in range(100):
            i * i
            time.sleep(0.1)

if __name__ == '__main__':

    processes = []
    num_processes = os.cpu_count()
    print(f'cpu count is {num_processes}')

    # create processes
    for i in range(num_processes):
        p = Process(target=square_numbers)
        processes.append(p)

    # start
    for p in processes:
        p.start()

    # join
    for p in processes:
        p.join()

    print('end main')

# threading api
from threading import Thread
import os
import time

def square_numbers_thread():
     for i in range(100):
          i * i
          time.sleep(0.1)

threads = []
num_threads = 10

# create threads
for i in range(num_threads):
     t = Thread(target=square_numbers)
     threads.append(t)

# start
for t in threads:
     t.start()

# join
for t in threads:
     t.join()