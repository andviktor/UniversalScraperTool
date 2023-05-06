from multiprocessing.pool import ThreadPool

from functools import wraps
import time
import random

class Thread:
    """Creates a thread pool

        Params:
        func (function) - any function
        data (list) - a list with data for different tasks
            example a list of urls:
            data = [
                'https://test1.com/',
                'https://test2.com/'
            ]
        concurrency (int) - the number of concurrencies, default 1
    """
    def __init__(self, func, data, concurrency=1, delay=0):
        self._func = func
        self._data = data
        self._concurrency = concurrency
        self._delay = delay

    def set_delay(self, delay):
        self._delay = delay

    def run(self):
        delays = [self._delay * random.randint(1,5) for x in range(len(self._data))]
        random.shuffle(delays)
        arguments = zip(delays, self._data)
        pool = ThreadPool(self._concurrency) 
        pool.starmap(self.middle_func, arguments)
        pool.close() 
        pool.join()

    def middle_func(self, delay, *args, **kwargs):
        time.sleep(delay)
        return self._func(*args, **kwargs)