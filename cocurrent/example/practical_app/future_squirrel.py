import concurrent.futures
import time

from cocurrent.example.practical_app.utils import check_website, WEBSITE_LIST

NUM_WORKERS = 4

if __name__ == '__main__':
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
        futures = {executor.submit(check_website, address) for address in WEBSITE_LIST}
        concurrent.futures.wait(futures)
        end_time = time.time()
    print("Time for FutureSquirrel: %ssecs" % (end_time - start_time))

# WARNING:root:Timeout expired for website http://really-cool-available-domain.com
# WARNING:root:Timeout expired for website http://another-really-interesting-domain.co
# WARNING:root:Website http://live.com returned status_code=405
# WARNING:root:Website http://bing.com returned status_code=405
# WARNING:root:Website http://netflix.com returned status_code=405
# Time for FutureSquirrel: 6.58627986907959secs
