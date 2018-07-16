import asyncio
import os
import time
import threading
import multiprocessing

SECS = 10
NUM_WORKERS = 4


def print_proc():
    print("PID: %s, Process Name: %s, Thread Name: %s" % (
        os.getpid(),
        multiprocessing.current_process().name,
        threading.current_thread().name)
          )


async def only_co_sleep():
    print_proc()
    try:
        await asyncio.sleep(SECS)
    except StopIteration:
        pass


async def co_sleep():
    start_time = time.time()
    tasks = [only_co_sleep() for _ in range(NUM_WORKERS)]
    await asyncio.wait(tasks)
    end_time = time.time()
    print("Coroutine time=", end_time - start_time)


def run_coroutin():
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(co_sleep())
    finally:
        event_loop.close()


def only_sleep():
    print_proc()
    time.sleep(SECS)


def run_serially():
    start_time = time.time()
    for _ in range(NUM_WORKERS):
        only_sleep()
    end_time = time.time()
    print("Serial time=", end_time - start_time)


def run_thread():
    start_time = time.time()
    threads = [threading.Thread(target=only_sleep) for _ in range(NUM_WORKERS)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    end_time = time.time()
    print("Threads time=", end_time - start_time)


def run_process():
    start_time = time.time()
    processes = [multiprocessing.Process(target=only_sleep()) for _ in range(NUM_WORKERS)]
    [process.start() for process in processes]
    [process.join() for process in processes]
    end_time = time.time()
    print("Parallel time=", end_time - start_time)


if __name__ == '__main__':
    run_serially()
    run_coroutin()
    run_thread()
    run_process()
