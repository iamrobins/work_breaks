from threading import Lock

class AppState:
    def __init__(self, break_over: bool):
        self.__break_over = break_over
        self.__quit = False
        self.__lock = Lock()

    #Add getter and setter to make accessing stuff in this object thread-safe

    def get_break_over(self) -> bool:
        self.__lock.acquire()
        result = self.__break_over
        self.__lock.release()
        return result

    def set_break_over(self, break_over: bool):
        self.__lock.acquire()
        self.__break_over = break_over
        self.__lock.release()

    break_over = property(get_break_over, set_break_over)

    def get_quit(self) -> bool:
        self.__lock.acquire()
        result = self.__quit
        self.__lock.release()
        return result

    def set_quit(self, quit: bool):
        self.__lock.acquire()
        self.__quit = quit
        self.__lock.release()

    quit = property(get_quit, set_quit)
