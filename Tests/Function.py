from Affirms import affirm, affirm_eq, affirm_ne
from TestDecorators import test
import sys
sys.path.append(r'C:\Users\Wannes\Desktop\JokNavi\2023\Coding\Python\PythonWrangler\V1')


class StupidClass:

    def add(self, left, right):
        return left + right

    def append(self, text, string):
        return text + string


@test
def test_add():
    SC = StupidClass()
    add_result = SC.add(1, 5)
    affirm_eq(add_result, 6)


@test
def test_append():
    SC = StupidClass()
    append_result = SC.append("Hi", " i'm nav!")
    affirm_eq(append_result, "Hi i'm nav")


if __name__ == "__main__":
    test_add()
    test_append()
