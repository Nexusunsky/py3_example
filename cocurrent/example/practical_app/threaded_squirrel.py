import threading
import time
from queue import Queue

from cocurrent.example.practical_app.utils import check_website, WEBSITE_LIST

NUM_WORKERS = 4
task_queue = Queue()


def worker():
    # Constantly check the queue for addresses
    while True:
        address = task_queue.get()
        check_website(address)
        # Mark the processed task as done
        task_queue.task_done()


if __name__ == '__main__':
    start_time = time.time()
    # Create the worker threads
    threads = [threading.Thread(target=worker) for _ in range(NUM_WORKERS)]
    # Add the websites to the task queue
    [task_queue.put(item) for item in WEBSITE_LIST]
    # Start all the workers
    [thread.start() for thread in threads]
    # Wait for all the tasks in the queue to be processed
    task_queue.join()
    end_time = time.time()

    print("Time for ThreadedSquirrel: %ssecs" % (end_time - start_time))

# WARNING:root:Timeout expired for website http://really-cool-available-domain.com
# WARNING:root:Timeout expired for website http://another-really-interesting-domain.co
# WARNING:root:Website http://live.com returned status_code=405
# WARNING:root:Website http://bing.com returned status_code=405
# WARNING:root:Website http://netflix.com returned status_code=405
# Time for ThreadedSquirrel: 4.901150941848755secs
