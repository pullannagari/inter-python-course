# detailed threading module
# how to share the data b/w threads
# locks to prevent race condition
# demon process
# queue for thread safe data exchanges

from threading import Thread, Lock, current_thread
import time
from queue import Queue
# global variable, to simulate a db variable
database_value = 0

def increase(lock):
    global database_value
    # get the lock and modify the value
    lock.acquire()
    local_copy = database_value

    # processing
    local_copy += 1
    # since the lock is acquired and lnot released, the second thread cannot acquire the lock until released
    time.sleep(0.1)
    database_value = local_copy
    # lock is released after the increment is written
    lock.release()

    # the recommended way of doing this is using context managers
    # with lock: this automatically acquires and releases the lock

def worker(q, lock):
    while True:
        value = q.get()
        # processing the queue element
        with lock:
            print(f"in {current_thread().name} got {value}")
        q.task_done()

if __name__ == "__main__":
    lock = Lock()
    print(f'start value: {database_value}')

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end value', database_value)

    # # queue is FIFO
    # q = Queue()

    # q.put(1)
    # q.put(2)
    # q.put(3)

    # # gets the first value and removes the element from the queue
    # first = q.get()

    # # we need to always call q.task_done after the processing for current element is done and can now continue
    # q.task_done()

    # # similar to join method
    # # waits until all the elements from the queue are gotten and processed
    # # blocks the main thread
    # q.join()

    # # check if a queue is empty
    # q.empty()

    q1 = Queue()

    num_threads = 10

    for i in range(num_threads):
        # create threads
        # pass lock as the argument 
        thread = Thread(target=worker, args=(q1,lock))
        # we use a daemon thread to run in the background and exit when the main thread exits
        thread.daemon = True
        thread.start()

    for i in range(1, 21):
        q1.put(i)

    q1.join()

    print('end main')

