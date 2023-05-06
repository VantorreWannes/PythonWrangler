import sys
sys.path.extend(["src/python_wrangler/test_types", "src/python_wrangler"])
from _test_function import function_wrapper
from _affirms import affirm, get_raised_type, AffirmError


@function_wrapper
def test_function_one(value):
    affirm(True)
    return value

@function_wrapper
def test_function_two():
    affirm(False)

if __name__ == "__main__":
    print(f"test_function_one: {test_function_one(True)}")
    print(f"test_function_one: {get_raised_type(test_function_two(), AffirmError)}")
