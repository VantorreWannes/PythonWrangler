import sys
import types


class AffirmError(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __get_new_traceback(self):
        try:
            raise self
        except BaseException:
            traceback = sys.exc_info()[2]
            return traceback

    def __trunicate_traceback(self, traceback: types.TracebackType, amount: int):
        back_frame = traceback.tb_frame
        for _ in range(0, amount):
            back_frame = back_frame.f_back
        return types.TracebackType(tb_next=None,
                                   tb_frame=back_frame,
                                   tb_lasti=back_frame.f_lasti,
                                   tb_lineno=back_frame.f_lineno)

    def __get_trunicated_error(self, amount):
        traceback = self.__get_new_traceback()
        trunicated_traceback = self.__trunicate_traceback(traceback, amount+3)
        return self.with_traceback(trunicated_traceback)
    
    def raise_to_level(self, amount=0):
        raise self.__get_trunicated_error(amount)


if __name__ == "__main__":
    AffirmError("Affirm returned False!").raise_to_level()
