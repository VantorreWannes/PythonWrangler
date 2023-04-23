import functools
from AffirmError import AffirmIsFalse


def test(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            if wrapper.verbose:
                print(f"|OK|: {func.__name__}")
        except AffirmIsFalse as err:
            if wrapper.verbose:
                print(f"|ER|: {func.__name__}")
            if wrapper.crash_on_false:
                err.raise_to_level(2)
    wrapper.crash_on_false: bool = True
    wrapper.verbose: bool = True
    wrapper.test = True
    return wrapper


def get_all_test_functions(cls):
    return [method for _, method in cls.__dict__.items() if hasattr(method, 'test')]


def test_all(cls, crash_on_false=True, verbose=True):
    for test_func in get_all_test_functions(cls):
        setattr(test_func, "verbose", False)
        try:
            test_func(cls())
            if verbose:
                print(f"|OK|: {cls.__name__}::{test_func.__name__}")
        except AffirmIsFalse as err:
            if verbose:
                print(f"|ER|: {cls.__name__}::{test_func.__name__}")
            if crash_on_false:
                err.raise_to_level(2)


def test_class(cls):
    cls.test_all = classmethod(test_all)
    return cls


if __name__ == "__main__":
    print("Ran")
