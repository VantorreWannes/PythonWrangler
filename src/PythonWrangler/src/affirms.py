
def raises(function: object, expected_exception: Exception, *args, **kwargs):
    """
    Checks if the raised error from the first parameter is equal to the expected exception.
    Checks for type if expected_exception is a type.
    Checks for equality if expected_exception is initiated.
    """
    try:
        function(*args, **kwargs)
    except BaseException as e:
        if isinstance(expected_exception, type):
            return isinstance(e, expected_exception)
        else:
            return isinstance(e, type(expected_exception)) and e.args == expected_exception.args

def is_true(contition: bool):
    if not isinstance(contition, bool):
        raise TypeError("Test condition should be of type: bool")

def test():
    raise IndexError("lol")

if __name__ == "__main__":
    print(raises(test, IndexError)) # True
    print(raises(test, IndexError("lol"))) # True
    print(raises(test, IndexError())) # False
    print(raises(test, IndexError("XD"))) # False

