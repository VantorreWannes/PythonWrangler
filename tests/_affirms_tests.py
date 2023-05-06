import sys
sys.path.extend(["src/python_wrangler"])
from _affirms import affirm, affirm_eq, raises
from _affirm_error import AffirmError

def raise_error(value):
    print(value)
    raise KeyError("no")

def test_raises():
    return raises(lambda: raise_error(1), KeyError)

if __name__ == "__main__":
    print(test_raises())
    


