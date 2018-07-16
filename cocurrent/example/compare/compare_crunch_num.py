import asyncio
import os
import time
import threading
import multiprocessing

NUM_WORKERS = 4


def print_proc():
    print("PID: %s, Process Name: %s, Thread Name: %s" % (
        os.getpid(),
        multiprocessing.current_process().name,
        threading.current_thread().name)
          )


async def co_crunch_numbers():
    print_proc()
    x = 0
    while x < 10000000:
        x += 1


async def co_compute():
    tasks = [co_crunch_numbers() for _ in range(NUM_WORKERS)]
    await asyncio.wait(tasks)


def run_coroutin():
    start_time = time.time()
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(co_compute())
    finally:
        event_loop.close()
    end_time = time.time()
    print("Coroutin time=", end_time - start_time)


def crunch_numbers():
    print_proc()
    x = 0
    while x < 10000000:
        x += 1


def run_serially():
    start_time = time.time()
    for _ in range(NUM_WORKERS):
        crunch_numbers()
    end_time = time.time()
    print("Serial time=", end_time - start_time)


def run_thread():
    start_time = time.time()
    threads = [threading.Thread(target=crunch_numbers) for _ in range(NUM_WORKERS)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    end_time = time.time()
    print("Threads time=", end_time - start_time)


def run_process():
    start_time = time.time()
    processes = [multiprocessing.Process(target=crunch_numbers) for _ in range(NUM_WORKERS)]
    [process.start() for process in processes]
    [process.join() for process in processes]
    end_time = time.time()
    print("Parallel time=", end_time - start_time)


if __name__ == '__main__':
    run_serially()
    run_coroutin()
    run_thread()
    run_process()
