class entry_exit(object):

    def __init__(self, f):
        self.f = f

    def __call__(self, *args):
        print("Entering", self.f.__name__)
        self.f(*args)
        print("Exited", self.f.__name__)

@entry_exit
def func1(a):
    print("inside func1()", a)

@entry_exit
def func2(a):
    print("inside func2()", a)

if __name__ == '__main__':
    func1(10)
    func2(15)