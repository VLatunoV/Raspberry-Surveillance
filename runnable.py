class Runnable:
    def __setup(self):
        pass

    def __cleanup(self):
        pass

    def __func(self, *args, **kw):
        pass

    def run(self, *args, **kw):
        self.__setup()
        try:
            self.__func(args, kw)
        finally:
            self.__cleanup()
