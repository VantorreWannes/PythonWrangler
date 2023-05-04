import sys
sys.path.append(r'YOUR PATH HERE')
from OLD.TestDecorators import test, test_class
from OLD.Affirms import affirm, affirm_eq, affirm_ne


def function_to_be_tested_1(left, right):
        return left + right

def function_to_be_tested_2(text, string):
        return text + string


def function_to_be_tested_3(left, right):
    return left > right

@test_class
class InsertClassHereTests:

    @test
    def test_function_1(self):
        add_result = function_to_be_tested_1(1, 5)
        affirm_eq(add_result, 6)

    @test
    def test_function_2(self):
        append_result = function_to_be_tested_2("Hi", " i'm nav!")
        affirm_eq(append_result, "Hi i'm nav")


    def other_function_1(self):
        print("this won't print")

@test
def test_function_3():
    is_larger_than = function_to_be_tested_3(6, 5)
    affirm(is_larger_than)


if __name__ == "__main__":
    InsertClassHereTests().test_all() #"crash_on_false" and "verbose" are 2 parameters both are set to True when left out.
    test_function_3() # the decorators are non configurable

