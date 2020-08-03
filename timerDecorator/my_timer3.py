import time

class entry_exit(object):
    def __init__(self, f):
        self.f = f

    def __call__(self, *args):
        t1 = time.time()
        result = self.f(*args)
        t2 = time.time() - t1
        print(f'11: {self.f.__name__} ran in {t2:.1f} seconds.')
        return result

@entry_exit
def anotherFunction(todo):
    time.sleep(2)
    print(f"17: anotherFunction()... run with arguments: ({todo})")

anotherFunction("shopping...")