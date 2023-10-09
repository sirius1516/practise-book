import time
from functools import wraps


def wait(seconds):
    def decor_function(function):
        @wraps(function)
        def wrap_function(*args, **kwargs):
            time.sleep(seconds)
            print(f'There was a pause {seconds} seconds before')
            return function(*args, **kwargs)
        return wrap_function
    return decor_function


@wait(5)
def wait_function(name):
    return f'Hello, {name}!'


print(wait_function('ISland'))
