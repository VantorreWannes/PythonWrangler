import sys
from typing import Any
sys.path.extend(["src/python_wrangler/test_types"])
from _test_class import TestClass
from _test_function import TestFunction
from _affirms import affirm
from functools import partial, wraps


def func_lol(value):
    return value + 1

if __name__ == "__main__":
    lol = func_lol(1)
    print(lol)


        