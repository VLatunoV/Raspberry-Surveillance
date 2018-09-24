class Runnable:
    def setup(self):
        print("Base setup")

    def cleanup(self):
        print("Base cleanup")

    def func(self, *args, **kw):
        print("Base func")

    def run(self, *args, **kw):
        self.setup()
        try:
            self.func(args, kw)
        finally:
            self.cleanup()
