import inspect
import sys
import types
sys.path.extend(["src/python_wrangler/test_types"])
from functools import wraps
from _test_class import TestClass
from _test_function import TestFunction
from _test_method import TestMethod


def test(*args, **kwargs):
    def parms_wrapper(crash_on_false=True, verbose=True):
        def wrapper(obj):
            if inspect.isclass(obj):
                obj = TestClass(obj, crash_on_false, verbose)
            elif obj.__name__ != obj.__qualname__:
                obj = TestMethod(obj, crash_on_false, verbose)
            elif inspect.isfunction(obj):
                obj = TestFunction(obj, crash_on_false, verbose)
            return obj
        return wrapper

    if len(args) == 1 and callable(args[0]):
        return parms_wrapper(True, True)(args[0])
    else:
        return parms_wrapper(*args, **kwargs)

if __name__ == "__main__":
    pass


        