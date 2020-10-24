class SuperClass:
    super1 = None
    super2 = None

    def __init__(self):
        self.field1 = 10
        self.field2 = "hello"

    def __repr__(self):
        return "(%d, %d, %s)" %(self.super1, self.field1, self.field2)

    def setField1(self,field):
        self.super3 = field

    def setField2(self, field):
        SuperClass.super1 = field

class SubClass(SuperClass):
    pass

x = SubClass()
y = SubClass()
SuperClass.super1 = 5
print("24:",x.super1)
print("25:",y.super1)

x.setField1(20)
print("28:",x)
print("31:",y)
print("29:",x.super1)
print("30:",y.super1)

x.setField2(30)
print("34:",x)
print("35:",y)
print("36:",x.super1)
print("37:",y.super1)

print("39:",SuperClass.super1)
print("40:",x)
print("41:",y)