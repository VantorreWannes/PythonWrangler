class RaisedWrongType(Exception):

    def __init__(self, actual_exception_type: BaseException, expected_exception_type: BaseException) -> None:
        self.message = f"Expression raised: {IndexError().__class__.__name__}, instead of expected: {TabError().__class__.__name__}."
        super().__init__(self.message)


if __name__ == "__main__":
    error = RaisedWrongType(type(IndexError()), type(TabError()))
    raise error
    