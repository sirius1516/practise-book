from functools import wraps

def my_function(function):
    @wraps(function)
    def wrap_function(*args, **kwargs):
        print(args, ' -This is args')
        print(kwargs, ' -This is kwargs')
        return function(*args, **kwargs)
    return wrap_function


@my_function
def new_function():
    print('My homework is done!')


new_function()
