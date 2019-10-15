"""demo for  the threading"""

import threading
from time import sleep
from random import random


def worker(delay):
    """thread function"""
    t_name = threading.current_thread().name
    t_id = threading.current_thread().ident
    # sleep(delay)
    print(t_name, 'waited for the :', delay)   # critical section


def main():
    """main thread"""
    list_of_threads = []

    for item in range(1, 6):
        rand_value = random()
        t = threading.Thread(target=worker, args=(rand_value,), name=f't{item}')
        list_of_threads.append(t)
        t.start()

    for t in list_of_threads:
        t.join()

    print(threading.current_thread().name, 'prepares to terminates')


if __name__ == '__main__':
    main()
