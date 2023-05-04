import functools
from _affirm_error import AffirmError


def _test_function(func, crash_on_false: bool, verbose: bool,  *args, **kwargs):
    try:
        func(*args, **kwargs)
    except AffirmError as err:
        if verbose:
            print(f"|ER|: {func.__name__}")
        if crash_on_false:
            raise err.get_trunicated_error(1)
    else:
        if verbose:
            print(f"|OK|: {func.__name__}")


def _test_all(cls: object, crash_on_false: bool = True, verbose: bool = True):
    for _, method in cls.__dict__.items():
        if hasattr(method, "_test_function"):
            _test_function(method, crash_on_false, verbose)


def test(obj):
    if isinstance(obj, type):
        @functools.wraps(obj)
        def wrapped_class(*args, **kwargs):
            return obj
        setattr(obj, "test_all", classmethod(_test_all))
        return wrapped_class
    else:
        @functools.wraps(obj)
        def wrapped_function(*args, **kwargs):
            wrapped_function._test_function(obj, True, True, *args, **kwargs)
        wrapped_function._test_function = _test_function
        return wrapped_function
    
if __name__ == "__main__":
    pass