import time
import datetime as dt

def timer(func):
    def wrapper_func(*args, **kwargs):
        print("start")
        tic = time.perf_counter()
        # tic = dt.datetime.now()
        func(*args,*kwargs)
        # toc = dt.datetime.now()
        toc = time.perf_counter()
        elapsed = toc - tic
        print("End")
        print(f'time taken to run {func.__name__!r} was {elapsed:.3f} s')
    return wrapper_func

@timer
def longRunningProcess(count:int):
    for i in range(count):
        sum([i**2 for i in range(count)])

longRunningProcess(100)