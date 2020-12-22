'''
dynamically assign a new method to existing object

'''
from types import MethodType

class MyObj(object):
    def __init__(self, val):
        self.val = val

def new_method(self, value):
    return self.val + value

obj = MyObj(3)

#rename the method new_method to be added defined in obj instance.
obj.add = MethodType(new_method, obj)
print(obj.add(5))
