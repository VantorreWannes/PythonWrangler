import sys
import types


class AffirmIsFalse(BaseException):
    # Exception raised if the result of the affirm function is False.
    def __init__(self, message="Affirm retured False!"):
        self.message = message

    def get_trunicated_traceback(self, amount=1):
        try:
            raise self
        except AffirmIsFalse:
            traceback = sys.exc_info()[2]
            back_frame = traceback.tb_frame
            for _ in range(0, amount):
                back_frame = back_frame.f_back
            return types.TracebackType(tb_next=None,
                                       tb_frame=back_frame,
                                       tb_lasti=back_frame.f_lasti,
                                       tb_lineno=back_frame.f_lineno)
    
    def raise_to_level(self, amount = 1):
        traceback = self.get_trunicated_traceback(amount+1)
        raise self.with_traceback(traceback)



if __name__ == "__main__":
    ERROR = AffirmIsFalse("test")
    ERROR.raise_to_level(1)
