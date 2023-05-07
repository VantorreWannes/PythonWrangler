from collections import OrderedDict
from functools import wraps
from _test_method import TestMethod
import inspect


class TestClass:

    def __init__(self, cls, crash_on_false: bool, verbose: bool) -> None:
        self._cls = cls
        self._test_methods = self._get_test_methods()
        self.crash_on_false = crash_on_false
        self.verbose = verbose

    def __getattr__(self, name):
        return getattr(self._cls, name)

    def __call__(self, *args, **kwargs):
        return self._cls(*args, **kwargs)

    @staticmethod
    def __is_test_method(method):
        return isinstance(method, TestMethod)

    @staticmethod
    def __has_no_parameters(method):
        params = inspect.signature(method).parameters
        return len([param for param in params.values() if param.default == param.empty]) == 1

    def _get_test_methods(self):
        return [method for method in self._cls.__dict__.values() if self.__is_test_method(method) and self.__has_no_parameters(method)]


if __name__ == "__main__":
    pass
