import inspect
from src.__internals.testable_types.testable_class import TestableClass
from src.__internals.testable_types.testable_function import TestableFunction
from src.__internals.testable_types.testable_method import TestableMethod
from src.__internals.testable_types.testable_settings import TestableSettings


def test(*args, **kwargs):
    """
    The test decorator applies both its settings to the wrapped object. (Class, method, function)
    Those settings are:
        - crash_on_false; Which decides if an AffirmError from the affirm functions should be raised again or neglected.
        - verbose; Which decides if it should print out the result of the wrapped object or not. (OK or ER + obj path)
    
    The test objects can have explicit or unexplicit settings.
    Settings are explicit if they are manually set in the test decorator call.
    Settings are unexplicit if they are left out, or no brackets are provided all together.
    Test decorator setting priority works like this:
        - If a setting is explicit all settings of the same type underneath are set to that value.
        - The topmost call gets priority to set explicit settings first.
        - if settings are inexplicit they are set to their default value unless overwritten by higher level settings. (Default value is True for both settings)
    """

    def parms_wrapper(crash_on_false=None, verbose=None):
        settings = TestableSettings(
            (("crash_on_false", crash_on_false), ("verbose", verbose))
        )

        def wrapper(obj):
            if inspect.isclass(obj):
                obj = TestableClass(obj, settings)
            elif obj.__name__ != obj.__qualname__:
                obj = TestableMethod(obj, settings)
            elif inspect.isfunction(obj):
                obj = TestableFunction(obj, settings)
            return obj

        return wrapper

    if len(args) == 1 and callable(args[0]):
        return parms_wrapper()(args[0])
    else:
        return parms_wrapper(*args, **kwargs)


if __name__ == "__main__":
    pass
