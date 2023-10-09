from functools import wraps

def prohibit_more_than_2_args(function):
    @wraps(function)
    def wrap_function(*args, **kwargs):
        if len(args) < 3:
            return function(*args, **kwargs)
        else:
            raise ValueError('Function must have less than 3 arguments')
    return wrap_function


@prohibit_more_than_2_args
def prohibited_args(*args, **kwargs):
    return "Good job! There are 2 args"


print(prohibited_args('Indira', 'Sergey'))
