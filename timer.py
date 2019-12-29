from functools import wraps
import time


def timer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print('>' * 20, 'start ...')
        start_time = time.time()
        result = func(*args, **kwargs)
        elapse_time = time.time() - start_time
        print('<' * 20, 'elapse times:', elapse_time)
        return result
    return inner
