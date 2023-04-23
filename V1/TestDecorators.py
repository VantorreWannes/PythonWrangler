from AffirmError import AffirmIsFalse

def test(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            if wrapper.verbose:
                print(f"|OK|: {func.__name__}")
        except AffirmIsFalse as err:
            if wrapper.verbose:
                print(f"|ER|: {func.__name__}")
            if wrapper.crash_on_false:
                err.raise_to_level(2)
    wrapper.crash_on_false: bool = True
    wrapper.verbose: bool = True
    return wrapper


if __name__ == "__main__":
    print("Ran")
