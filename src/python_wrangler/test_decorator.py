import inspect
from _affirm_error import AffirmError

@staticmethod
def _test_function(func, crash_on_false: bool, verbose: bool, *args, **kwargs):
    try:
        func()
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
        if hasattr(attr, "_test_function"):
            _test_function(attr, crash_on_false, verbose)


def test(obj):
    if isinstance(obj, type):
        setattr(obj, "test_all", _test_all)
        return obj
    else:
        setattr(obj, "_test_function", (_test_function))
        return obj


if __name__ == "__main__":
    pass
