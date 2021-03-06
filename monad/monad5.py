from pymonad.operators.maybe import Just
from pymonad.reader import Compose

list1=[1,2,3,4,5]
def head(alist):
    return [alist[0],]

def tail(alist):
    return alist[1:]

head1 = head(list1)
print("14: header: ",head1)
print("15:",type(head1))

tail1 = tail(list1)
print("18: tail: ", tail1)

new_func = Compose(tail).then(head) #链式运行结构
# apply tail first on the list, and then apply head to the result of tail.
print("23: ", new_func(list1))
