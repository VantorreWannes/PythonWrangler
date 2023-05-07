class TestSettings:

    def __init__(self, crash_on_false, verbose) -> None:
        self.crash_on_false = crash_on_false
        self.verbose = verbose

    
    def with_defaults(self, crash_on_false_default: bool, verbose_default: bool):
        crash_on_false = crash_on_false_default if self.crash_on_false == None else self.crash_on_false
        verbose = verbose_default if self.verbose == None else self.verbose
        return crash_on_false, verbose