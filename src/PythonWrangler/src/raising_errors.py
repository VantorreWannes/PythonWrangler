import sys
import types


class RaisingError:

    def __init__(self, error: BaseException) -> None:
        self.error = error

    def _get_new_traceback(self):
        try:
            raise self.error
        except BaseException:
            traceback = sys.exc_info()[2]
            return traceback

    def _trunicate_traceback(self, traceback: types.TracebackType, amount: int):
        back_frame = traceback.tb_frame
        for _ in range(0, amount):
            back_frame = back_frame.f_back
        return types.TracebackType(tb_next=None,
                                   tb_frame=back_frame,
                                   tb_lasti=back_frame.f_lasti,
                                   tb_lineno=back_frame.f_lineno)

    def raise_to_level(self, amount=0):
        traceback = self._get_new_traceback()
        trunicated_traceback = self._trunicate_traceback(traceback, amount+2)
        raise self.error.with_traceback(trunicated_traceback)


if __name__ == "__main__":
    RaisingError(IndexError("Index testing out of bounds!")).raise_to_level()
