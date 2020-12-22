import random

class C:
    def __init__(self,count):
        self.count = count

    def __repr__(self):
        return str(self.count)

    def __lt__(self, other):
        return self.count < other.count

longList = [C(random.random()) for i in range(10)]
longList.sort()
#longList.sort(key = lambda c: c.count)
print(longList)