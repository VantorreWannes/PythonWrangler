from functools import partial, wraps

def _pseudo_decor(fun, argument):
    # magic sauce to lift the name and doc of the function
    @wraps(fun)
    def ret_fun(*args, **kwargs):
        # pre function execution stuff here, for eg.
        print("decorator argument is %s" % str(argument))
        returned_value =  fun(*args, **kwargs)
        # post execution stuff here, for eg.
        print("returned value is %s" % returned_value)
        return returned_value

    return ret_fun

real_decorator1 = partial(_pseudo_decor, argument="some_arg")
real_decorator2 = partial(_pseudo_decor, argument="some_other_arg")


@real_decorator1
def bar(*args, **kwargs):
    return 1


if __name__ == "__main__":
    bar(1,2,3, k="v", x="z")