import sys
sys.path.extend(["src", "src\python_wrangler", "src\python_wrangler\_test_functions"])
from python_wrangler import affirm, affirm_eq, affirm_ne, test
from _test_functions import TestMethod, TestFunction


def function_wrapper(func):
    def wrapper(*args, **kwargs):
        return TestMethod(func, True, True).test(*args, **kwargs)
    return wrapper

def method_wrapper(func):
    def wrapper(*args, **kwargs):
        return TestMethod(func, True, True).test(*args, **kwargs)
    return wrapper

@function_wrapper
def my_function(value=1):
    affirm(True)
    return value

class MyClass:

    @method_wrapper
    def my_method(self, value=1):
        affirm(True)
        return value
    
if __name__ == "__main__":
    my_function_value, my_method_value = my_function(10), MyClass().my_method(5)
    print("return value:", my_function_value)
    print("return value:", my_method_value)