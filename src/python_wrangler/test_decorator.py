import functools
import inspect
from _affirm_error import AffirmError

def _test_function(func, method = False,  crash_on_false: bool = True, verbose: bool = True, *args, **kwargs):
    try:
        if method:
            func(func, *args, **kwargs)
        else:
            func(*args, **kwargs)
    except AffirmError as err:
        if verbose:
            print(f"|ER|: {func.__name__}")
        if crash_on_false:
            raise err.get_trunicated_error(1)
    else:
        if verbose:
            print(f"|OK|: {func.__name__}")


def _test_all(self, crash_on_false: bool = True, verbose: bool = True):
    for _, attr in inspect.getmembers(self, predicate=inspect.ismethod):
        if hasattr(attr, "_is_test"):
            _test_function(attr, True, crash_on_false, verbose)


def test(obj):
    if isinstance(obj, type):
        setattr(obj, "test_all", _test_all)
        return obj
    else:
        @functools.wraps(obj)
        def wrapper(*args, **kwargs):
            return _test_function(obj, *args, **kwargs)
        setattr(wrapper, "_is_test", True)
        return wrapper


if __name__ == "__main__":
    pass
