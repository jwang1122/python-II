from types import MethodType

class MyObj(object):
    def __init__(self, val):
        self.val = val

def new_method(self, value):
    return self.val + value

#obj = MyObj(3)
#obj.add = MethodType(new_method, obj)

#print(obj.add(5))

MyObj.add = MethodType(new_method, MyObj)
print(type(MyObj.add))
obj2 = MyObj(6)
print(obj2.add(8))