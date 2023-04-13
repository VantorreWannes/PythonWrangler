import inspect
from Logging import Log, LogLevel


class AffirmIsFalse(BaseException):
    # Exception raised if the result of the affirm function is False.
    def __init__(self, message="Affirm retured False!"):
        self.message = message
        super().__init__(self.message)


def affirm_ne(item, item2):
    if not item != item2:
        raise AffirmIsFalse()


def affirm_eq(item, item2):
    if not item == item2:
        raise AffirmIsFalse()


def affirm(item):
    caller_function = inspect.getframeinfo(
        inspect.currentframe().f_back).function
    is_test = hasattr(caller_function, "is_test")
    if not item:
        if is_test:
            raise AffirmIsFalse()
        else:
            caller_function.log.error("Affirm failed.")
            return None
    else:
        caller_function.log.ok("Affirm Test succeeded..")
        return None


# function decorator to be applied to any function you want to test in
def test(func, crash_on_error=False, verbose=True):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            wrapper.log.ok("Test succeeded.")
        except AffirmIsFalse as e:
            wrapper.log.error("Test failed.")
            if wrapper.crash_on_error:
                raise e

    wrapper.log = Log(
        func.__name__, LogLevel=LogLevel.INFO if verbose else LogLevel.QUIET)
    wrapper.is_test = True
    wrapper.crash_on_error = crash_on_error
    return wrapper


if __name__ == "__main__":
    pass
