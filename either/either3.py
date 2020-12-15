from pymonad.either import Left, Right
from pymonad.operators import *
from pymonad.operators.maybe import Just

"""
bind function list, terminated during error out in the middle.
重要的 Web Service 编程理念：
    任何service都返回两种可能性：1. 成功； 2. 失败
    一旦失败，service立即带着错误信息返回。
    最终成功：service带着成功结果返回。
功能块驱动理念：
    将眼光聚焦在所要完成任务都一系列操作上，将这些操作链接起来（bind）

"""
def isEven(x):
    if (type(x) not in [int]):
        reason = ('Error', 'The input value {0} is not an interger.'.format(x))
        return Left(reason)
    if (x % 2 == 0):
        return Right(x)
    reason = ('Error', "The x=%d mod of 2 equals 1." % x)
    return Left(reason)


def add5(x):
    if (x == 0):
        reason = ('Error', "The x=0.")
        return Left(reason)
    return Right(x + 5)


def sub4(x):
    if x >= 10:
        return Right(x - 4)
    reason = ('Error', f"x = {x} < 10")
    return Left(reason)


print("36:", isEven(3).bind(add5))
print("37:", isEven(4).bind(add5))
print("38:", isEven(5).bind(add5).bind(sub4))
print("39:", isEven(4).bind(sub4).bind(add5).bind(sub4))
print("40:", Right(10).bind(isEven).bind(sub4).bind(add5))


def f1(x):  
    # define all things need to do in a chain, if-else still in place of each function
    return isEven(x).bind(sub4).bind(add5).bind(sub4).bind(add5)

print("47:", f1(2.3+4j))
print("48:", f1(11).value)
print("49:", f1(12))
print("50:", f1(4))
