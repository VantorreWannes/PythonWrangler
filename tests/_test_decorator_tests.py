import sys
sys.path.extend(["src"])
from python_wrangler import affirm, affirm_eq, affirm_ne, test


@test(crash_on_false=False, verbose=False)
def test_function_one(value=0):
    affirm(False)
    return value+1

@test
def test_function_two(value=0):
    affirm(True)
    return value+1

@test
class TestClass:

    def __init__(self) -> None:
        pass
        
    @test
    def test_method_one(self, value=0):
        affirm(True)
        return value+1
    
    @test(False)
    def test_method_two(self, value=0):
        affirm(False)
        return value+1


if __name__ == "__main__":
    print("FUNCTIONS:", end="\n\n")
    function_one_value = test_function_one(0)
    function_two_value = test_function_two(1)
    print(f"function_one_value: {function_one_value}")
    print(f"function_two_value: {function_two_value}")
    print("METHODS:", end="\n\n")
    TEST_CLASS = TestClass()
    method_one_value = TEST_CLASS.test_method_one(0)
    method_two_value = TEST_CLASS.test_method_two(1)
    print(f"method_one_value: {method_one_value}")
    print(f"method_two_value: {method_two_value}")
    print("TEST_ALL:", end="\n\n")
    TestClass().test_all()
    