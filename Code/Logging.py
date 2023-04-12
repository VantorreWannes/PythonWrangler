from enum import Enum
import time

class LogLevel(Enum):
    INFO = 1
    OK = 2
    ERROR = 3
    QUIET = 100000

class Log:
    def __init__(self, name="Logger", LogLevel=LogLevel.INFO) -> None:
        self.name = name
        self.level = LogLevel
    
    def time(self):
        return time.ctime(time.time())

    def set_level(self, new_log_level):
        self.level = new_log_level
    
    def print_log(self, level, text):
        if level.value >= self.level.value:
            print(f"|({self.time()})::{self.name}::{level.name}|: {text}")    

    def info(self, text):
        self.print_log(LogLevel.INFO, text)
    
    def error(self, text):
        self.print_log(LogLevel.ERROR, text)
    
    def ok(self, text):
        self.print_log(LogLevel.OK, text)


if __name__ == "__main__":
    LOG = Log("TestLogger", LogLevel.INFO)
    LOG.info("Test info!")
    LOG.error("Test error!")
    LOG.set_level(LogLevel.QUIET)
    LOG.error("Oops..")
