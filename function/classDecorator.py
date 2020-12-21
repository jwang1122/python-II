"""
dunder __call__
understand function decorator

"""
class my_decorator(object):

    def __init__(self, f):
        print("\ninside my_decorator.__init__()")
        f() # Prove that function definition has completed

    def __call__(self):
        print("inside my_decorator.__call__()")

@my_decorator
def aFunction():
    print("inside aFunction()")

if __name__ == '__main__':
    aFunction()

    print("Finished decorating aFunction()")

