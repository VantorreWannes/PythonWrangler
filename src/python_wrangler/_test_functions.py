from abc import ABC, abstractmethod
from _affirm_error import AffirmError


class _TestFunctionsIterface(ABC):

    def __init__(self, func, crash_on_false: bool, verbose: bool) -> None:
        self._func = func
        self._function_path = self._get_function_path()
        self._crash_on_false = crash_on_false
        self._verbose = verbose
    
    def _get_function_path(self):
        function_path: str = self._func.__qualname__
        return [part for part in function_path.split(".")]

    @abstractmethod
    def _print_result(self, prefix: str):
        pass

    def _failed(self, err: AffirmError):
        if self._verbose:
            self._print_result("ER")
        if self._crash_on_false:
            raise err.get_trunicated_error(2)
    
    def _success(self):
        if self._verbose:
            self._print_result("OK")
    
    @abstractmethod
    def test(self):
        pass

class TestFunction(_TestFunctionsIterface):

    def __init__(self, func, crash_on_false: bool, verbose: bool) -> None:
        super().__init__(func, crash_on_false, verbose)
    
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

class TestMethod(_TestFunctionsIterface):

    def __init__(self, func, crash_on_false: bool, verbose: bool) -> None:
        super().__init__(func, crash_on_false, verbose)
    
    def _print_result(self, prefix: str):
        method_path = "::".join(self._function_path)
        print(f"|{prefix}|: {method_path}")

    def test(self, *args, **kwargs):
        try:
            return_value = self._func(*args, **kwargs)
        except AffirmError as err:
            self._failed(err)
        else:
            self._success()
        return return_value





        
        
