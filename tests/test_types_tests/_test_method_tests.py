import sys
sys.path.extend(["src/python_wrangler/test_types", "src/python_wrangler"])
from _test_method import method_wrapper
from _affirms import affirm


@method_wrapper
def test_method_one(value):
    affirm(True)
    return value

if __name__ == "__main__":
    print(f"test_function_one: {test_method_one('Returned value!')}")