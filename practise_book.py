from functools import wraps

def hello_from_decorator(function):
    @wraps(function)
    def wrap_function(*args, **kwargs):
        firstname = function(*args, **kwargs)
        return str(firstname) + ' Hello from decorator!'
    return wrap_function


@hello_from_decorator
def first_name_function():
    return 'sirius1516'


print(first_name_function())