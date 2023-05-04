from affirm_error import AffirmError


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

def affirm(contition: bool):
    if not isinstance(contition, bool):
        raise TypeError("Test condition should be of type: bool.")
    if not contition:
        raise AffirmError("Affirm is False.").get_trunicated_error(1)

def affirm_eq(item_one, item_two):
    if not item_one == item_two:
        raise AffirmError("Item one and two are not equal.").get_trunicated_error()
    
def affirm_ne(item_one, item_two):
    if not item_one != item_two:
        raise AffirmError("Item one and two are equal.").get_trunicated_error()

if __name__ == "__main__":
    affirm_eq(IndexError, IndexError)
    affirm_ne(IndexError(), IndexError)

