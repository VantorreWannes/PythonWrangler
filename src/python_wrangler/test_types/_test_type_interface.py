import sys
sys.path.extend(["src/python_wrangler"])
from abc import ABC, abstractmethod
from _affirm_error import AffirmError

class TestTypeIterface(ABC):

    def __init__(self, func, crash_on_false: bool, verbose: bool) -> None:
        self._func = func
        self._function_path = self._get_function_path()
        self.crash_on_false = crash_on_false
        self.verbose = verbose
    
    def _get_function_path(self):
        function_path: str = self._func.__qualname__
        return [part for part in function_path.split(".")]

    @abstractmethod
    def _print_result(self, prefix: str):
        pass

    def _failed(self, err: AffirmError):
        if self.verbose:
            self._print_result("ER")
        if self.crash_on_false:
            raise err.get_trunicated_error(2)
    
    def _success(self):
        if self.verbose:
            self._print_result("OK")
    
    @abstractmethod
    def test(self):
        pass

if __name__ == "__main__":
    pass