# def myassert(condition):
#     """Throw AssertionError with modified traceback if condition is False."""
#     if condition:
#         return

#     # This function ... is not guaranteed to exist in all implementations of Python.
#     # https://docs.python.org/3/library/sys.html#sys._getframe
#     # back_frame = sys._getframe(1)
#     try:
#         raise AssertionError
#     except AssertionError:
#         traceback = sys.exc_info()[2]
#         back_frame = traceback.tb_frame.f_back

#     back_tb = types.TracebackType(tb_next=None,
#                                   tb_frame=back_frame,
#                                   tb_lasti=back_frame.f_lasti,
#                                   tb_lineno=back_frame.f_lineno)
#     raise AssertionError().with_traceback(back_tb)

"""Modify traceback on exception.

See also https://github.com/python/cpython/commit/e46a8a
"""

import sys
import types


def test(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
    return inner

def is_true(case):
    try:
        assert case
    except AssertionError:
        traceback = sys.exc_info()[2]
        back_frame = traceback.tb_frame.f_back.f_back # each .f_back skips one call
        back_tb = types.TracebackType(tb_next=None,
                                      tb_frame=back_frame,
                                      tb_lasti=back_frame.f_lasti,
                                      tb_lineno=back_frame.f_lineno)
        raise AssertionError().with_traceback(back_tb)

def affirm(one, two):
    is_true(one==two)


@test
def example():
    affirm(1, 2)


if __name__ == "__main__":
    example()
