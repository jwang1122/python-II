"""
Use ListMonad create list, then do then() or map()
仅解决了链式运作的问题，但没有解决出现意外的问题。
"""
from pymonad.list import *
from pymonad.operators.maybe import Just, Nothing

list0 = ListMonad(1,2,3,4)
print("09:", type(list0))
print("10:", type(list0[2]))
print(list0[2])

def neg(x):
    return -x

def add3(x):
    return x+3

print("19:", list0.map(neg)) # Functor 允许普通的功能块使用map作用与打包的变量，如List，Just（4），我们希望我们已有的功能块能够处理打包的变量。
print("20:", list(map(lambda x: -x, list0)))    # 普通情况下map的使用，用lambda表达式给出功能块定义。
print("21:",list(map(neg, list0)))     # 通情况下map的使用，用预先定义的功能块
print("22:", list0.map(add3)) 

x = list0.then(neg).then(add3) #链式运行结构
print("25:",x) 

x = list0.then(add3).then(neg) #链式运行结构
print("28:",x) 

print("30:", add3 * (neg * Just(9))) #链式运行结构

# list0 = ListMonad(1,2,3,4,None)
# x = list0.then(add3).then(neg) #链式运行结构
# print("34:",x) 
