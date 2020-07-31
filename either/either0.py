"""
Return boxed tuple message.

isEven() function return either Right(success) or Lift(error)
"""
from pymonad import *

def isEven(x):
    if(type(x) not in [int]):
        reason = ('Error', 'The input value {0} is not an interger.'.format(x))
        return Left(reason)
    if(x % 2 == 0):
        reason = ('Success',"The x=%d mod of 2 is 0." % x)
        return Right(reason)
    reason = ('Error',"The x=%d mod of 2 equals 1." % x)
    return Left(reason)

print(isEven(4))
print(isEven(7))
print(isEven(3.2))
print(isEven(3+2j))
print(isEven(-2))
print("Done.")