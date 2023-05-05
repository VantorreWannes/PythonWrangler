import functools
import inspect
from _affirm_error import AffirmError


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
