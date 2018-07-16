import multiprocessing
import time

from cocurrent.example.practical_app.utils import check_website, WEBSITE_LIST

NUM_WORKERS = 4

if __name__ == '__main__':
    start_time = time.time()
    with multiprocessing.Pool(processes=NUM_WORKERS) as pool:
        results = pool.map_async(check_website, WEBSITE_LIST)
        results.wait()
    end_time = time.time()

    print("Time for MultiProcessingSquirrel: %ssecs" % (end_time - start_time))

# WARNING:root:Timeout expired for website http://really-cool-available-domain.com
# WARNING:root:Timeout expired for website http://another-really-interesting-domain.co
# WARNING:root:Website http://live.com returned status_code=405
# WARNING:root:Website http://netflix.com returned status_code=405
# WARNING:root:Website http://bing.com returned status_code=405
# Time for MultiProcessingSquirrel: 5.281938314437866secs
