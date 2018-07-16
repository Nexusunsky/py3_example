import os
import time
import threading
import multiprocessing

NUM_WORKERS = 4


def only_sleep():
    """ Do nothing, wait for a timer to expire """
    print("PID: %s, Process Name: %s, Thread Name: %s" % (
        os.getpid(),
        multiprocessing.current_process().name,
        threading.current_thread().name)
          )
    time.sleep(1)


def run_serially():
    global start_time, end_time
    # Run tasks serially
    start_time = time.time()
    for _ in range(NUM_WORKERS):
        only_sleep()
    end_time = time.time()
    print("Serial time=", end_time - start_time)


def run_thread():
    global start_time, end_time
    # Run tasks using threads
    start_time = time.time()
    threads = [threading.Thread(target=only_sleep) for _ in range(NUM_WORKERS)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    end_time = time.time()
    print("Threads time=", end_time - start_time)


def run_process():
    global start_time, end_time
    # Run tasks using processes
    start_time = time.time()
    processes = [multiprocessing.Process(target=only_sleep()) for _ in range(NUM_WORKERS)]
    [process.start() for process in processes]
    [process.join() for process in processes]
    end_time = time.time()
    print("Parallel time=", end_time - start_time)


if __name__ == '__main__':
    run_serially()
    run_thread()
    run_process()

# PID: 6355, Process Name: MainProcess, Thread Name: MainThread
# PID: 6355, Process Name: MainProcess, Thread Name: MainThread
# PID: 6355, Process Name: MainProcess, Thread Name: MainThread
# PID: 6355, Process Name: MainProcess, Thread Name: MainThread
# Serial time= 4.0040059089660645
# PID: 6355, Process Name: MainProcess, Thread Name: Thread-1
# PID: 6355, Process Name: MainProcess, Thread Name: Thread-2
# PID: 6355, Process Name: MainProcess, Thread Name: Thread-3
# PID: 6355, Process Name: MainProcess, Thread Name: Thread-4
# Threads time= 1.0056109428405762
# PID: 6355, Process Name: MainProcess, Thread Name: MainThread
# PID: 6355, Process Name: MainProcess, Thread Name: MainThread
# PID: 6355, Process Name: MainProcess, Thread Name: MainThread
# PID: 6355, Process Name: MainProcess, Thread Name: MainThread
# Parallel time= 4.018326997756958
