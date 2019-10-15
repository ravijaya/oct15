"""demo for  the thread sync using semaphore"""

import threading
from time import sleep
from random import random
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s : %(message)s')


def worker(delay, lock):
    """thread function"""
    sleep(delay)
    t_name = threading.current_thread().name
    t_id = threading.current_thread().ident

    logging.debug('checking for the lock')

    with lock:
        logging.debug('acquired the lock')

        print(t_name, 'waited for the :', delay)  # critical section
        sleep(1)
        logging.debug('releases the lock')


def main():
    """main thread"""
    list_of_threads = []
    lock_object = threading.Semaphore(1)  # binary semaphore aka mutex

    for item in range(1, 6):
        rand_value = random()
        t = threading.Thread(target=worker, args=(rand_value, lock_object))
        list_of_threads.append(t)
        t.start()

    for t in list_of_threads:
        t.join()

    print(threading.current_thread().name, 'prepares to terminates')


if __name__ == '__main__':
    main()
