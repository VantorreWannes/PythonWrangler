# PythonWrangler tests!
## Introduction

This library includes decorators and affirm functions that can be used to write unit tests in Python. The library is designed to be easy to use and to facilitate the creation of test cases that can be run automatically.

### Dependencies

- Python 3.x
- TestDecorators
- Affirms

### Installation

1. Clone the repository and navigate to the directory
2. Install dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

### Usage

1. Import the necessary modules at the top of your Python file:

   ```
   from TestDecorators import test, test_class
   from Affirms import affirm, affirm_eq, affirm_ne
   ```

2. Define the function you want to test. For example:
3. 
   ```
   def function_to_be_tested_1(left, right):
       return left + right
   ```

4. Write a test for the function using the `test` decorator:

   ```
   @test
   def test_function_1(self):
       add_result = function_to_be_tested_1(1, 5)
       affirm_eq(add_result, 6)
   ```

5. If you have multiple tests, you can group them together in a class using the `test_class` decorator:

   ```
   @test_class
   class InsertClassHereTests:
       @test
       def test_function_1(self):
           add_result = function_to_be_tested_1(1, 5)
           affirm_eq(add_result, 6)
       @test
       def test_function_2(self):
           append_result = function_to_be_tested_2("Hi", " i'm nav!")
           affirm_eq(append_result, "Hi i'm nav")
   ```

6. If you have a test function that is not part of a class, you can use the `test` decorator without the `@test_class` decorator:

   ```
   @test
   def test_function_3():
       is_larger_than = function_to_be_tested_3(6, 5)
       affirm(is_larger_than)
   \```

7. To run all tests, use the `test_all()` command:

   ```
   if __name__ == "__main__":
       InsertClassHereTests().test_all()
   ```

### Example

Here is an example of how your Python file could look like:

```
from TestDecorators import test, test_class
from Affirms import affirm, affirm_eq, affirm_ne

def function_to_be_tested_1(left, right):
    return left + right

@test
def test_function_1():
    add_result = function_to_be_tested_1(1, 5)
    affirm_eq(add_result, 6)

@test_class
class InsertClassHereTests:
    def function_to_be_tested_2(text, string):
        return text + string

    @test
    def test_function_2(self):
        append_result = function_to_be_tested_2("Hi", " i'm nav!")
        affirm_eq(append_result, "Hi i'm nav")

@test
def test_function_3():
    is_larger_than = function_to_be_tested_3(6, 5)
    affirm(is_larger_than)

if __name__ == "__main__":
    InsertClassHereTests().test_all()
```

### Conclusion

This library is a useful tool for testing Python code and ensuring that it works as expected. By following the steps outlined in this README, you can easily write unit tests for your code and ensure that it is working as intended.


