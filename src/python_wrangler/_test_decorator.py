import inspect
import sys
import types
sys.path.extend(["src/python_wrangler/test_types"])
from _test_class import TestClass
from _test_function import TestFunction
from _test_method import TestMethod
from _settings import TestTypeSettings

def test(*args, **kwargs):
    def parms_wrapper(crash_on_false=None, verbose=None):
        settings = TestTypeSettings((("crash_on_false", crash_on_false), ("verbose", verbose)))
        def wrapper(obj):
            if inspect.isclass(obj):
                obj = TestClass(obj, settings)
            elif obj.__name__ != obj.__qualname__:
                obj = TestMethod(obj, settings)
            elif inspect.isfunction(obj):
                obj = TestFunction(obj, settings)
            return obj
        return wrapper

    if len(args) == 1 and callable(args[0]):
        return parms_wrapper()(args[0])
    else:
        return parms_wrapper(*args, **kwargs)

if __name__ == "__main__":
    pass


        