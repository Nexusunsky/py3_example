import threading
import time
from queue import Queue
from random import random

q = Queue()


def double_task(n):
    return n * 2


def producer():
    while 1:
        wt = random()
        time.sleep(wt)
        q.put(double_task, wt)


def consumer():
    while 1:
        task, arg = q.get()
        print(arg, task(arg))
        q.task_done()


if __name__ == '__main__':
    for target in (producer, consumer):
        t = threading.Thread(target=target)
        t.start()
