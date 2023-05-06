from functools import wraps

# def doublewrap(f):
#     @wraps(f)
#     def new_dec(*args, **kwargs):
#         if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
#             return f(args[0])
#         else:
#             return lambda realf: f(realf, *args, **kwargs)
#     return new_dec

# @doublewrap
# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner

# @make_pretty()
# def ordinary():
#     print("I am ordinary")


# @make_pretty
# def ordinary_too():
#     print("I am ordinary")

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


def make_special(func):
    @wraps(func)
    def inner(*args, **kwargs):  # To allow automatic func input
        print("Decorating...")
        return func(*args, **kwargs)  #4
    return inner  #2


@make_special  #1
def decorated(value):
    print("I am decorated!")  
    return value  #5

def undecorated(value):
    print("I am undecorated!")  
    return value  #5


if __name__ == "__main__":
    value = decorated("OK decorated")  #3
    print(value, end="\n\n")  #6
    value = make_special(undecorated)("OK undecorated")
    print(value, end="\n\n")

