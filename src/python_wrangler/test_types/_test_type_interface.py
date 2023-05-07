import sys
sys.path.extend(["src/python_wrangler"])
from abc import ABC, abstractmethod
from _affirm_error import AffirmError
from _settings import TestTypeSettings

class TestTypeIterface(ABC):

    def __init__(self, func, settings: TestTypeSettings) -> None:
        self._func = func
        self._function_path = self._get_function_path()
        self.settings = settings
    
    def _get_function_path(self):
        function_path: str = self._func.__qualname__
        return [part for part in function_path.split(".")]

    @abstractmethod
    def _print_result(self, prefix: str):
        pass

    def _failed(self, err: AffirmError):
        if self.settings.get_or("verbose", True):
            self._print_result("ER")
        if self.settings.get_or("crash_on_false", True):
            raise err.get_trunicated_error(2)
    
    def _success(self):
        if self.settings.get_or("verbose", True):
            self._print_result("OK")
    
    @abstractmethod
    def test(self):
        pass

if __name__ == "__main__":
    pass