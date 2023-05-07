from _test_method import TestMethod
from _affirm_error import AffirmError
import inspect


class TestClass:

    def __init__(self, cls, crash_on_false: bool, verbose: bool) -> None:
        self._cls = cls
        setattr(self._cls, "test_all", self._test_all)
        self._crash_on_false = crash_on_false
        self._verbose = verbose

    def __getattr__(self, name):
        return getattr(self._cls, name)

    def __call__(self, *args, **kwargs):
        return self._cls(*args, **kwargs)

    @staticmethod
    def __has_no_parameters(method):
        params = inspect.signature(method).parameters
        result = len([param for param in params.values() if param.default == param.empty]) == 1
        return result

    def _get_test_methods(self):
        return [method for method in self._cls.__dict__.values() if isinstance(method, TestMethod) and self.__has_no_parameters(method)]
    
    def _test_all(self):
        test_methods = self._get_test_methods()
        for method in test_methods:
            method.crash_on_false = self._crash_on_false
            method.verbose = self._verbose
            try:
                method()
            except AffirmError as err:
                raise err.get_trunicated_error(0)

if __name__ == "__main__":
    pass
