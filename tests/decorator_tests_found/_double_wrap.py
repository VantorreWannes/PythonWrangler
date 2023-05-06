from functools import wraps

def doublewrap(f):
    @wraps(f)
    def new_dec(*args, **kwargs):
        if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
            return f(args[0])
        else:
            return lambda realf: f(realf, *args, **kwargs)
    return new_dec

@doublewrap
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty()
def ordinary(value):
    print("I am ordinary")
    print(value)


@make_pretty
def ordinary_too(value):
    print("I am ordinary")
    print(value)


ordinary()
ordinary_too(1)
