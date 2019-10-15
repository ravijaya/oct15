"""demo for  the threading"""

import threading
import subprocess

threads_value = dict()


def worker(job):
    """thread function"""
    response = subprocess.check_output(job).decode()
    threads_value[tuple(job)] = response

"""http://collabedit.com/k32ht"""
def main():
    """main thread"""
    list_of_threads = []

    for item in [['python', 'psgrepme.py'], ['ipconfig']]:
        t = threading.Thread(target=worker, args=(item,))
        list_of_threads.append(t)
        t.start()

    for t in list_of_threads:
        t.join()

    for job, response in threads_value.items():
        print(job, '->', response)
        print()


if __name__ == '__main__':
    main()
