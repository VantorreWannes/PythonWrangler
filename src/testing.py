from python_wrangler.affirms import affirm, affirm_eq, affirm_ne
from python_wrangler.test_decorator import test


def add_function_to_be_tested(left, right):
    return left + right

add_result = add_function_to_be_tested(1, 5)
affirm(add_result == 6) # affirm functions check if the statement equates to True. And by default they will crash on False.

def test_function_1():
    add_result = add_function_to_be_tested(1, 5)
    affirm(add_result > 0) # This function is not decorated with @test and therefore works exactly like the 2 statements above test_function_1()

@test # Functions can be decorated with @test to make them print their outcome, OK or ER; after running.
def test_function_2():
    add_result = add_function_to_be_tested(1, 5)
    affirm_eq(add_result, 6) # affirm_eq() behaves like affirm but will its outcome be decided by if the two parameters are equal.

@test # Classes can also be wrapped with @test in order to add a special method to them, test_all().
class AddFunctionTests:

    @test
    def test_function_3(self):
        add_result = add_function_to_be_tested(1, 5)
        affirm_ne(add_result, -1) 
    
    def not_a_test_function(self):
        print("this won't print on test_all()")
    
if __name__ == "__main__":
    test_function_1() 
    test_function_2() # @test wrapped functions propegate their traceback upwards to the line they are called from
    test_class = AddFunctionTests()
    test_class.test_function_3()