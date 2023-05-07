from _test_method import TestMethod
from _affirm_error import AffirmError
import inspect
from _settings import TestTypeSettings


class TestClass():

    def __init__(self, cls, settings: TestTypeSettings) -> None:
        self._cls = cls
        self.settings = settings
        setattr(self._cls, "test_all", self._test_all)

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
            method_old_settings = method.settings
            if self.settings.get_all() != (None, None):
                method.settings = self.settings
            try:
                method()
                method.settings = method_old_settings
            except AffirmError as err:
                method.settings = method_old_settings
                raise err.get_trunicated_error(0)
                

if __name__ == "__main__":
    pass
