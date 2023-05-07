from _affirm_error import AffirmError
from functools import wraps
from operator import methodcaller as mc


def raises(func, error_type: Exception):
    try:
        func()
    except error_type:
        return True
    except Exception:
        return False
    else:
        return False


def affirm(contition: bool):
    if not isinstance(contition, bool):
        raise TypeError("Test condition should be of type: bool.")
    if not contition:
        raise AffirmError("Affirm is False.").get_trunicated_error()

def affirm_eq(item_one, item_two):
    if not item_one == item_two:
        raise AffirmError("Item one and two are not equal.").get_trunicated_error()
    
def affirm_ne(item_one, item_two):
    if not item_one != item_two:
        raise AffirmError("Item one and two are equal.").get_trunicated_error()

if __name__ == "__main__":
    affirm_eq(IndexError, IndexError)
    affirm_ne(IndexError, IndexError)

