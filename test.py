def my_wrapper(func):
    def wrapper(*args, **kwargs):
        # do something before calling the original function
        result = func(*args, **kwargs)
        # do something after calling the original function
        return result
    
    # Add a custom attribute to the wrapper function
    wrapper.is_wrapped = True
    
    return wrapper

#@my_wrapper
def my_function():
    pass


if hasattr(my_function, 'is_wrapped') and my_function.is_wrapped:
    print('my_function is wrapped')
else:
    print('my_function is not wrapped')


