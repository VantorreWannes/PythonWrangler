from contextlib import contextmanager
from src.__internals.affirm_error import AffirmError

@contextmanager
def raises(expected_exception: Exception):
    try:
        yield
    except expected_exception:
        pass
    except Exception as e:
        raise e


def affirm(contition: bool):
    """
    Raises an AffirmError if the given condition is False.
    """
    if not isinstance(contition, bool):
        raise TypeError("Test condition should be of type: bool.")
    if not contition:
        raise AffirmError("Affirm is False.").get_trunicated_error()

def affirm_eq(item_one, item_two):
    """
    Checks to make sure the two items are equal, and raises an AffirmError otherwise.
    """
    if not item_one == item_two:
        raise AffirmError("Item one and two are not equal.").get_trunicated_error()
    
def affirm_ne(item_one, item_two):
    """
    Raises an AffirmError if the two items are equal.
    """
    if not item_one != item_two:
        raise AffirmError("Item one and two are equal.").get_trunicated_error()

if __name__ == "__main__":
    pass