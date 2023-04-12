IDEA:
- Create a Wrapper function hijacking any test commands happening inside the function.
- [affirm(item), affirm_eq!(item), affirm_ne!(item)]
- Add a --always_test argument to enable or disable running the tests on packages compiled for release
- Add the ability to add a @test_class decorator above a class which returns the class with a test_all() command to run all the tests inside that class.
- Add settings for crash on False and if the function should log a message