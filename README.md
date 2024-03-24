# **PythonWrangler**

This library includes decorators and affirm functions that can be used to write unit tests in Python. 
All tools provided in this package are designed to be easy to use and well suited for newer developers.

### `Dependencies`

- Python >=3.6

# Examples
Written below are some quick examples on each of the tools provided inside the PythonWrangler package.

### **!!** `First do this:` **!!**
Import the commands from the package as follows.<br>
```py
from python_wrangler import affirm, affirm_eq, affirm_ne, test
```

### `Affirm`
The affirm functions are quite easy to use and understand.
- `Affirm(condition)` crashes if the condition equates to False, and does nothing on True.
- `affirm_eq(item_1, item_2)` checks if the 2 parameters are equal, and crashes if they are not equal.
- `Affirm_ne(item_1, item_2)` checks if the 2 parameters are *not* equal, and crashes if they are equal

```py
affirm(3 == 3) # Does nothing
affirm(2 == 3) # Raises AffirmError

affirm_eq("Test", "Test") # Does nothing
affirm_eq("Hi", "Test") # Raises AffirmError

affirm_ne(10, 10) # Raises AffirmError
affirm_ne(5, 10) # Does nothing
```

### `Test`
The test decorator applies both its settings to the wrapped object. (Class, method, function)
Those settings are:
    - crash_on_false; Which decides if an AffirmError from the affirm functions should be raised again or neglected.
    - verbose; Which decides if it should print out the result of the wrapped object or not. (OK or ER + obj path)

The test objects can have explicit or implicit settings.
Settings are explicit if they are manually set in the test decorator call.
Settings are implicit if they are left out, or no brackets are provided all together.
Test decorator setting priority works like this:
    - Higher level explicit settings take precedence over lower level implicit settings.

### `Showcase`

```python
from python_wrangler import affirm, affirm_eq, affirm_ne, test

def add_one(left: int):
    return left + 1


@test
def test_function():
    #Checks to see if the statement resolves to True.
    affirm(add_one(0) == 1)
    #Checks for equality.
    affirm_eq(1, 1)
    #Checks for non-equality.
    affirm_ne(1, 2)
    # Will throw an AffirmError if an error of type Exception is not thrown inside its scope.
    with raises(Exception):
        raise Exception("TestException")

#Here crash_on_false is set to False and verbose is set to True. 
#Since the test methods are inside the scope of the class, the test methods don't crash on false.
@test(False, True) 
class TestClass(object):

    @test()
    def test_method(self):
        affirm(1 < 2)
        affirm_eq(1, 1)
        affirm_ne(1, 2)

    #This function overwrites TestClass' explicit don't-crash-on-affirm-error setting.
    @test(True, True)
    def other_test_method(self):
        affirm(1 == 2)
        
    #This method doesn't have a test decorator so it doesn't get recognised as a test function.
    #The affirms inside this method will work with default behavior. 
    #This method will not get run when the test_all() method is used.
    def undetected_method(self):
        affirm(1 == 2)


if __name__ == "__main__":
    test_function()
    TestClass().test_method()
    #Test all can be used to test all test methods inside of a test class.
    TestClass().test_all()

```