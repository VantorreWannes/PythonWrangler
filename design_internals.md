# PythonWrangler

## Feature functions:
- `raised(func, *args, **kwargs)`  #returns ExceptionType 
- `affirm(case)`  #asserts case equates to True and raises AffirmError on False
- `affirm_eq(case_1, case_2)`  #asserts case_1 and case_2 are equal and raises AffirmError if not
- `affirm_ne(case_1, case_2)`  #asserts case_1 and case_2 are not equal and raises AffirmError if they are equal
- `@test(crash_on_false, verbose)` #returns TestObject and the topmost test wrapper always has explicit parameter priority
  
## Background functionality:
- `TestObject(crash_on_false, verbose)` # Has a test method to test all containing TestObjects