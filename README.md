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
Test objects can have Explicit or unexplicit settings. 