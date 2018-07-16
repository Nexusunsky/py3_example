import os
import time
import threading
import multiprocessing

NUM_WORKERS = 4


def crunch_numbers():
    """ Do some computations """
    print("PID: %s, Process Name: %s, Thread Name: %s" % (
        os.getpid(),
        multiprocessing.current_process().name,
        threading.current_thread().name)
          )
    x = 0
    while x < 10000000:
        x += 1


def run_serially():
    global start_time, end_time
    start_time = time.time()
    for _ in range(NUM_WORKERS):
        crunch_numbers()
    end_time = time.time()
    print("Serial time=", end_time - start_time)


def run_thread():
    global start_time, end_time
    start_time = time.time()
    threads = [threading.Thread(target=crunch_numbers) for _ in range(NUM_WORKERS)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    end_time = time.time()
    print("Threads time=", end_time - start_time)


def run_process():
    global start_time, end_time
    start_time = time.time()
    processes = [multiprocessing.Process(target=crunch_numbers) for _ in range(NUM_WORKERS)]
    [process.start() for process in processes]
    [process.join() for process in processes]
    end_time = time.time()
    print("Parallel time=", end_time - start_time)


if __name__ == '__main__':
    run_serially()
    run_thread()
    run_process()
# PID: 6376, Process Name: MainProcess, Thread Name: MainThread
# PID: 6376, Process Name: MainProcess, Thread Name: MainThread
# PID: 6376, Process Name: MainProcess, Thread Name: MainThread
# PID: 6376, Process Name: MainProcess, Thread Name: MainThread
# Serial time= 2.6639418601989746
# PID: 6376, Process Name: MainProcess, Thread Name: Thread-1
# PID: 6376, Process Name: MainProcess, Thread Name: Thread-2
# PID: 6376, Process Name: MainProcess, Thread Name: Thread-3
# PID: 6376, Process Name: MainProcess, Thread Name: Thread-4
# Threads time= 3.2389180660247803
# PID: 6379, Process Name: Process-1, Thread Name: MainThread
# PID: 6380, Process Name: Process-2, Thread Name: MainThread
# PID: 6381, Process Name: Process-3, Thread Name: MainThread
# PID: 6382, Process Name: Process-4, Thread Name: MainThread
# Parallel time= 0.7041177749633789
