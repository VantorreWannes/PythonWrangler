from PythonWrangler import affirm, test, raises, AffirmError

@test(False, True)
class TestClass(object):

    @test()
    def test_method(self):
        affirm(1 == 1)

    @test(True, True)
    def other_test_method(self):
        with raises(AffirmError):
            affirm(1 == 0)

    def undetected_method(self):
        affirm(1 == 0)

if __name__ == '__main__':
    TestClass().test_all()
