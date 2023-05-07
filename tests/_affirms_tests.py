import sys
sys.path.extend(["src/python_wrangler"])
from _affirms import affirm, affirm_eq, affirm_ne, raises
from _affirm_error import AffirmError

def raise_error(value):
    raise KeyError("no")

def test_raises():
    return raises(lambda: raise_error(1), KeyError)

def test_affirm():
    affirm(1+1 == 2)
    affirm(True)

def test_affirm_eq():
    affirm_eq(1, 1)
    affirm_eq(AffirmError, AffirmError)

if __name__ == "__main__":
    affirm(test_raises())
    test_affirm()
    test_affirm_eq()
    


