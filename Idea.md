IDEA:
- Create a Wrapper function hijacking any test commands happening inside the function.
- [assert!(item), assert_eq!(item), assert_ne!(item)]
- Add a --always_test argument to enable or disable running the tests on packages compiled for release
- Add the ability to add a @test_class decorator above a class which returns the class with a try() command to run all the tests inside that class.