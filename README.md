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

### `Affirm`
The affirm functions are quite easy to use and understand.
- Affirm(condition) crashes if the condition equates to False, and does nothing on True.
- affirm_eq checks if the 2 parameters are equal, and crashes if they are not equal.
- Affirm_ne checks if the 2 parameters are *not* equal, and crashes if they are equal

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

The test objects can have explicit or unexplicit settings. <br>
Settings are explicit if they are manually set in the test decorator call.
Settings are unexplicit if they are left out, or no brackets are provided all together.
Decorator setting priority works like this:
  - If a setting is explicit all settings of the same type underneath are set to that value.
  - The topmost call gets priority to set explicit settings first.
  - if settings are inexplicit they are set to their default value unless overwritten by higher level settings. (Default value is True for both settings) 

### `Showcase`

```py
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
    TestClass().test_all() #Test all can be used to test all test methods inside of a test class.
    #TestClass().unaffected()

```