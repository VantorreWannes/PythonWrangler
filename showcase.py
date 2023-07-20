import sys
sys.path.extend(["src", "src\python_wrangler"])
from python_wrangler import affirm, affirm_eq, affirm_ne, test


def add_plus_one(left: int):
    return left + 1


@test
def test_function():
    #Checks to see if the statement resolves to True.
    affirm(add_plus_one(0) < 2)
    #Checks for equality.
    affirm_eq(1, 1)
    #Checks for non-equality.
    affirm_ne(1, 2)

#Here crash_on_false is set to False and verbose is set to True. 
#Since the test methods are inside the scope of the class, the test methods don't crash on false.
@test(False, True) 
class TestClass(object):

    @test()
    def test_method(self):
        affirm(True)
        affirm_eq(1, 1)
        affirm_ne(1, 2)

    #Here crash_on_false is explicitly set to True but it doesn't matter because it has been overwritten by TestClass's test settings. 
    @test(True, True)
    def other_test_method(self):
        affirm(False)
        
    #This method doesn't have a test decorator so it doesn't get recognised as a test function. The affirms inside this method will work with default behavior.
    def unaffected(self):
        affirm(False)


if __name__ == "__main__":
    test_function()
    TestClass().test_method()
    TestClass().test_all()
    #TestClass().unaffected()
