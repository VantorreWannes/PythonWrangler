from Logging import Log, LogLevel


class AffirmIsFalse():
    # Exception raised if the result of the affirm function is False.
    def __init__(self, message="Affirm retured False!"):
        self.message = message
        self.value = False


# function decorator to be applied to any function you want to test in
def test(crash_on_error=False, verbose=True):
    def test_decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, AffirmIsFalse):
                if wrapper.verbose:
                    wrapper.log.error(result.message)
                if wrapper.crash_on_error:
                    exit()
                return result
            elif not wrapper.is_affirm:
                wrapper.log.info(f"Test {func.__name__} succeeded.")

        wrapper.log = Log(func.__name__, LogLevel=LogLevel.INFO if verbose else LogLevel.QUIET)
        wrapper.crash_on_error = crash_on_error
        wrapper.verbose = verbose
        wrapper.is_affirm = func.__name__ in ["affirm", "affirm_eq", "affirm_ne"]
        return wrapper
    return test_decorator

@test()
def affirm_ne(item, item2, error_message="Affirm_ne returned False."):
    if item != item2:
        return True
    return AffirmIsFalse(error_message)

@test()
def affirm_eq(item, item2, error_message="Affirm_eq returned False."):
    if item == item2:
        return True
    return AffirmIsFalse(error_message)

@test()
def affirm(item, error_message="Affirm returned False."):
    if item:
        return True
    return AffirmIsFalse(error_message)


if __name__ == "__main__":
    affirm(False)
