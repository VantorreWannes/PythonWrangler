from functools import wraps

# GOAL 1:
#     @test
#     def test_func(self, value):
#         affirm(True)
#         return value

# GOAL 2:
#     @test(True, False)
#     def test_func(self, value):
#         affirm(false)
#         return value



def decorator_factory(*args, **kwargs):
    def actual_decorator(boolean_1=False, boolean_2=False):
        def wrapper(func):
            @wraps(func)
            def inner_wrapper(*func_args, **func_kwargs):
                print(boolean_1, boolean_2)
                result = func(*func_args, **func_kwargs)
                return result
            return inner_wrapper
        return wrapper

    if len(args) == 1 and callable(args[0]):
        return actual_decorator(False, False)(args[0])
    else:
        return actual_decorator(*args, **kwargs)

@decorator_factory
def decorated(value):
    print("I am decorated!")
    return value

@decorator_factory(True)
def decorated_with_arguments(a, b):
    print("I am decorated with arguments!")
    return a + b


if __name__ == "__main__":
    value = decorated_with_arguments(1, 5)
    print(f"Value: {value}", end="\n\n")
