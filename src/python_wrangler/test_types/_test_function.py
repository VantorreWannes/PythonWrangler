from functools import wraps
from _affirm_error import AffirmError
from _test_type_interface import TestTypeIterface

class TestFunction(TestTypeIterface):

    def __init__(self, func, crash_on_false: bool, verbose: bool) -> None:
        super().__init__(func, crash_on_false, verbose)

    def __getattr__(self, name):
        return getattr(self._func, name)
    
    def __call__(self, *args, **kwargs):
        return self.test(*args, **kwargs)
    
    def _print_result(self, prefix: str):
        function_path = "::".join(self._function_path)
        print(f"|{prefix}|: {function_path}")

    def test(self, *args, **kwargs):
        try:
            return_value = self._func(*args, **kwargs)
        except AffirmError as err:
            self._failed(err)
        else:
            self._success()
        return return_value
    
    
def function_wrapper(func):
    return TestFunction(func, True, True)
    
if __name__ == "__main__":
    pass
