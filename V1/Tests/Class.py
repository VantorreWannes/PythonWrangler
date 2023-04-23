from TestDecorators import test, test_class
from Affirms import affirm, affirm_eq, affirm_ne
import sys
sys.path.append(
    r'C:\Users\Wannes\Desktop\JokNavi\2023\Coding\Python\PythonWrangler\V1')


class StupidClass:

    def add(self, left, right):
        return left + right

    def append(self, text, string):
        return text + string


@test_class
class TestStupidClass:

    @test
    def test_add(self):
        SC = StupidClass()
        add_result = SC.add(1, 5)
        affirm_eq(add_result, 6)

    @test
    def test_append(self):
        SC = StupidClass()
        append_result = SC.append("Hi", " i'm nav!")
        affirm_eq(append_result, "Hi i'm nav")

    def test_print(self):
        print("this won't print")


if __name__ == "__main__":
    TSC = TestStupidClass()
    TSC.test_all(False)
