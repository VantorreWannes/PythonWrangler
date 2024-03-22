from src.PythonWrangler.__internals.affirm_error import AffirmError
from src.PythonWrangler.__internals.testable_types.testable_interface import TestableIterface
from src.PythonWrangler.__internals.testable_types.testable_settings import TestableSettings


class TestableMethod(TestableIterface):

    def __init__(self, func, settings: TestableSettings) -> None:
        super().__init__(func, settings)

    def __getattr__(self, name):
        return getattr(self._func, name)
    
    def __call__(self, *args, **kwargs):
        return self.test(*args, **kwargs)
    
    def _print_result(self, prefix: str):
        method_path = "::".join(self._function_path)
        print(f"|{prefix}|: {method_path}")

    def test(self, *args, **kwargs):
        try:
            return_value = self._func(self._func, *args, **kwargs)
        except AffirmError as err:
            self._failed(err)
            return None
        else:
            self._success()
        return return_value
    
if __name__ == "__main__":
    pass