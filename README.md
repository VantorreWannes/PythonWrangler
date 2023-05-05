# **PythonWrangler**

This library includes decorators and affirm functions that can be used to write unit tests in Python. 
All tools provided in this package are designed to be easy to use and well suited for newer developers.

### `Dependencies`

- Python 3.x
- Pypi


# Examples
Written below are some quick examples on each of the tools provided inside the PythonWrangler package.

### **!!** `First do this:` **!!**
Import the commands from the package as follows.<br>
```py
from python_wrangler import affirm, affirm_eq, affirm_ne, test
```
### `Info:`
For clarity's sake; I'll be using this definition of function_to_be_tested to run our tests on.
```py
def function_to_be_tested(left, right):
    return left + right
```

**All examples from now on have this code attached.** <br>
*These 4 lines have been left out of each following example.*
```py
from python_wrangler import affirm, affirm_eq, affirm_ne, test

def function_to_be_tested(left, right):
    return left + right
```

### `affirm:`
- Does nothing if the statement equates to True.
- Crashes if the statement equates to False. (Raises AffirmError)
- Doesn't log anything.
```py
result = function_to_be_tested(1, 5) # result is 6
affirm(result > 5) # Is True, does nothing
affirm(result == 6) # Is True, does nothing
affirm(result < 0) # Is False, crashes
```

### `affirm_eq:`
- Does nothing if the 2 statements are equal.
- Crashes if the 2 statements are not equal. (Raises AffirmError)
- Doesn't log anything.
```py
result = function_to_be_tested(1, 5) # result is 6
affirm_eq(result, 6) # Is equal, does nothing
affirm_eq(result, 10) # Is not equal, crashes
```

### `affirm_ne:`
- Opposite of `affirm_eq`.
- Does nothing if the 2 statements are not equal.
- Crashes if the 2 statements are equal. (Raises AffirmError)
- Doesn't log anything.
```py
result = function_to_be_tested(1, 5) # result is 6
affirm_ne(result, 10) # Is not equal, does nothing
affirm_ne(result, 6) # Is equal, crashes
```

### `@test:` (Function)

- Does nothing if AffirmError wasn't raised.
- Crashes if AffirmError was raised.
- Prints the result of the function. (|Status-code|: function_name)
```py

@test
def test_function_1():
    result = function_to_be_tested(1, 5) # result is 6
    affirm(result > 0) # Is True, does nothing
    affirm_eq(result, 6) # Is equal, does nothing

@test
def test_function_2():
    result = function_to_be_tested(1, 5) # result is 6
    affirm(result > 0) # Is True, does nothing
    affirm_eq(result, 11) # Is not equal, crashes

test_function_1() # Will print: "|OK|
test_function_2() 

```



