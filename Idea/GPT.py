"""Modify traceback on exception.

See also https://github.com/python/cpython/commit/e46a8a
"""

import sys
import types


def myassert(condition):
    """Throw AssertionError with modified traceback if condition is False."""
    if condition:
        return

    # This function ... is not guaranteed to exist in all implementations of Python.
    # https://docs.python.org/3/library/sys.html#sys._getframe
    # back_frame = sys._getframe(1)
    try:
        raise AssertionError
    except AssertionError:
        traceback = sys.exc_info()[2]
        back_frame = traceback.tb_frame.f_back

    back_tb = types.TracebackType(tb_next=None,
                                  tb_frame=back_frame,
                                  tb_lasti=back_frame.f_lasti,
                                  tb_lineno=back_frame.f_lineno)
    raise AssertionError().with_traceback(back_tb)


def myassert_false():
    """Test myassert(). Debugger should point at the next line."""
    myassert(False)


if __name__ == "__main__":
    myassert_false()