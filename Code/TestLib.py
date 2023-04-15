from Logging import Log, LogLevel


class AffirmIsFalse(BaseException):
    # Exception raised if the result of the affirm function is False.
    def __init__(self, message="Affirm retured False!"):
        self.message = message
        super().__init__(self.message)


# function decorator to be applied to any function you want to test in
def test(crash_on_error=False, verbose=True):
    def test_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs) 
                if not wrapper.is_affirm:
                    wrapper.log.info("Test succeeded.")
            except AffirmIsFalse as e:
                if not wrapper.is_affirm:
                    wrapper.log.error("Test failed.")
                if crash_on_error or wrapper.is_affirm:
                    raise e
                
        wrapper.log = Log(func.__name__, LogLevel=LogLevel.INFO if verbose else LogLevel.QUIET)
        wrapper.is_affirm = func.__name__ in ["affirm", "affirm_eq", "affirm_ne"]
        wrapper.crash_on_error = crash_on_error
        return wrapper
    return test_decorator

@test()
def affirm_ne(item, item2):
    if not item != item2:
        raise AffirmIsFalse()

@test()
def affirm_eq(item, item2):
    if not item == item2:
        raise AffirmIsFalse()

@test()
def affirm(item):
    if not item:
        raise AffirmIsFalse()

if __name__ == "__main__":
    affirm(False)
