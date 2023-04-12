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
    if not item:
        raise AffirmIsFalse()

# function decorator to be applied to any function you want to test in
def test(func, crash_on_error=False, verbose=True):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            wrapper.log.ok(wrapper.success_message)
        except AffirmIsFalse as e:
            wrapper.log.error(wrapper.error_message)
            if wrapper.crash_on_error:
                raise e

    wrapper.log = Log(func.__name__, LogLevel=LogLevel.INFO if verbose else LogLevel.QUIET)
    wrapper.is_test = True
    wrapper.crash_on_error = crash_on_error
    wrapper.error_message = "Test failed."
    wrapper.success_message = "Test succeeded."
    return wrapper


if __name__ == "__main__":
    pass
