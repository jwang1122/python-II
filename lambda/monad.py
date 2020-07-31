from pymonad import *

# Functor "Just" implements fmap
# def sayHello(person):
#     return f"Hello, {person}!"

# print("07:", sayHello("John"))
# print("08:", sayHello(Just("World")))
# print(type(sayHello(Just("World"))))
# print("10:", sayHello * Just("World")) # Just是一个Functor，implement fmap功能块，使得普通的功能块可以使用*作用其上
# print(type(sayHello * Just("World")))
# print("12:", sayHello * Just(None))
# x = Just("Wang").fmap(sayHello)
# print("14:",x)

# # Applicative amap
@curry
def add(x, y):
    return x + y

x = add * Just(7) & Just(8) # Just是一个Applicative，implement amap功能块，使得打包功能块作用于其上*相当（，&相当，
print("22:",x)
# x = Just(7).fmap(add).amap(Just(8))
# print("24:",x)

# x = add(7, 8) # 打包的功能块可以正常使用
# print("27: ", end=' ')
# print(type(x))
# print("29: x =", x)

# x=add(Just(7), Just(8)) # 打包功能块可以直接接受打包变量
# print("32:", x)

# x=add(7)# 打包功能块可以先只传递一个变量
# print("35: ", end=' ')
# print(type(x))
# x=x (8)  # 再传递另外一个变量
# print("38: x = ", x)

# list1=[1,2,3,4,5]
# @curry
# def head(alist):
#     return alist[0]

# @curry
# def tail(alist):
#     return alist[1:]

# head1 = head(list1)
# print("50: header: ",head1)
# print("51:",type(head1))

# tail1 = tail(list1)
# print("54: tail: ", tail1)

# seq= head * tail  # apply tail first on the list, and then apply head to the result of tail.
# print("57: ", seq(list1))

# @curry
# def mul(x, y):
#     return x * y

# comp = add(7) * mul(2) # Combine 2 functions together, execute in squence
# x = comp(4)
# print("65: ",x)

# a=Nothing
# print("68:",a)
# #a.add()

# print('71: Hello, world.')

# list0 = List(1,2,3,4)
# print("74:", type(list0))
# print("75:", type(list0[2]))

# def neg(x):
#     return -x

# def add3(x):
#     return x+3

# print("83:", neg * list0) # Functor 允许普通的功能块使用*作用与打包的变量，如List，Just（4），我们希望我们已有的功能块能够处理打包的变量。
# print("84:", list(map(lambda x: -x, list1)))    # 普通情况下map的使用，用lambda表达式给出功能块定义。
# print("85:",list(map(neg, list1)))     # 通情况下map的使用，用预先定义的功能块
# print("86:", add3 * list0) 

# print("88:",neg * Just(9)) # 普通功能块处理打包变量
# list2=(Just(1), Just(2), Just(3))
# # x = neg * list2 # 把* 当作了乘法算符，而不是Functor算符
# x = add * Just(7) & Just(8) #打包功能块可以使用*类似括号，&类似逗号来作用与打包的变量Appicative，本来普通的功能块是不知道如何处理打包变量的，使用了*&后就可以了。
# print("92:",x)

# x = add * Nothing & Just(8)
# print("95:",x)

# x = mul * Just(2) & Just(3)
# print("98: ",x)

# def sub(x, y): #正常功能块
#     return x-y

# x = sub(10,4)
# print("104:", x)
# #x = sub * Just(10) & Just(4)  #正常功能块无法使用

# @curry #打包功能块
# def div(x, y):
#     return x/y if y else 0

# x = div(10, 0) # Return a normal int
# x=div * Just(10) & Just(4) # Applicative 打包功能作用于打包变量
# print("113:",x)

# def div(x:Just, y:Just):
#     return x/y
# #x=div(Just(10), Just(4)) # don't know how to calculate Just divided by Just

# print("119",add3 * Just(7))  #normal function apply on a Functor

# def positive_and_negative(x):
#     return List(x, -x)

# @curry
# def add_and_sub(x, y):
#     return List(y + x, y - x)

# # Monads allow you to sequence a series of calculations within than monad using the bind operator >>.
# x = List(2,3) >> positive_and_negative >> add_and_sub(3) 
# print("130:",x)

# x = Just(4) >>  positive_and_negative >> add_and_sub(3) 
# print("133:",x)

# def neg(x):
#     return List(-x)

# def add3(x):
#     return List(x+3)

# x= Just(7) >> neg >> add3
# print("142:",x)

# x = List(2,3) >> neg >> add3
# print("145:",x)

# @curry
# def div(x, y):
#     if(x is Nothing or y is Nothing):
#         return Just(Nothing)
#     return Just(x/y) if y else Just(Nothing)

# x = div(10,0)
# print("154:",x.getValue())

# x=div(10, Nothing)
# print("157:",x.getValue())

# x=div(10,4)
# print("160:", x.getValue())

# x = neg * Just(7)
# print("163:",x)

# from pymonad import *

# def neg(x):
#     return List(-x)

# def add3(x):
#     return List(x+3)

# list1 = List(1,2,3)
# x= Just(8) >> neg >> add3
# print("175:",x)

# x= Just(8) >> add3 >> neg
# print("178:",x)

# x=List(2, 5) >> neg >> add3
# print("181:",x)

