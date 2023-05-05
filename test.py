import inspect
import sys
sys.path.extend(["src", "src\python_wrangler"])
from python_wrangler import affirm, affirm_eq, affirm_ne, test


def function_to_be_tested(left, right):
    return left + right

@test
def first_test_function():
    affirm(True)

@test
def second_test_function():
    affirm(True)
    affirm(1+10 < 11)


@test
class FunctionToBeTestedTests(object):

    def __init__(self) -> None:
        pass

    @test
    def first_test_function(self):
        affirm(True)

    @test
    def second_test_function(self):
        affirm(True)
        affirm(False)


if __name__ == "__main__":
    FunctionToBeTestedTests().test_all()
