from src.PythonWrangler import affirm, test

@test
def test_affirm_implicit():
    affirm(1 == 1)

@test(crash_on_false=False, verbose=True)
def test_affirm_explicit():
    affirm(0 == 1)

if __name__ == '__main__':
    test_affirm_implicit()
    test_affirm_explicit()