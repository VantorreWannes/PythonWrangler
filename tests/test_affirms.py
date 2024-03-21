from src import affirm, affirm_ne, raises, affirm_eq, AffirmError

def add_one(left: int):
    return left + 1

def test_affirms():
    affirm(add_one(0) == 1)
    affirm_eq(add_one(0), 1)
    affirm_ne(add_one(0), 2)
    with raises(AffirmError):
        affirm(1 == 1)
    

if __name__ == '__main__':
    test_affirms()