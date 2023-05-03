from multiprocessing.pool import ThreadPool

def create_pool(func, data, concurrency=1):
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
    pool = ThreadPool(concurrency) 
    pool.map(func, data)
    pool.close() 
    pool.join()