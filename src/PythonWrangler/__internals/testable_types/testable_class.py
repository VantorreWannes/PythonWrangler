import inspect

from PythonWrangler.__internals.affirm_error import AffirmError
from PythonWrangler.__internals.testable_types.testable_method import TestableMethod
from PythonWrangler.__internals.testable_types.testable_settings import (
    TestableSettings,
)


class TestableClass:

    def __init__(self, cls, settings: TestableSettings) -> None:
        self._cls = cls
        self.settings = settings
        self._cls.test_all = self._test_all

    def __getattr__(self, name):
        return getattr(self._cls, name)

    def __call__(self, *args, **kwargs):
        return self._cls(*args, **kwargs)

    @staticmethod
    def __has_no_parameters(method):
        params = inspect.signature(method).parameters
        result = (
            len([param for param in params.values() if param.default == param.empty])
            == 1
        )
        return result

    def _get_test_methods(self):
        return [
            method
            for method in self._cls.__dict__.values()
            if isinstance(method, TestableMethod) and self.__has_no_parameters(method)
        ]

    def _test_all(self):
        test_methods = self._get_test_methods()
        for method in test_methods:
            method_old_settings = method.settings
            if self.settings.get_all() != (
                None,
                None,
            ) and method.settings.get_all() == (None, None):
                method.settings = self.settings
            try:
                method()
                method.settings = method_old_settings
            except AffirmError as err:
                method.settings = method_old_settings
                raise err.get_trunicated_error(0)


if __name__ == "__main__":
    pass
