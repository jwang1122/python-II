from pymonad.operators.maybe import Just
from pymonad.tools import curry

# # Applicative amap
@curry(2)
def add(x, y):
    return x + y

x = add * Just(7) & Just(8) 
# Just是一个Applicative，implement amap功能块，使得打包功能块作用于其上*相当()，&相当变量之间的逗号,
print("11:",x)
x = add(7, 8) # 打包的功能块可以正常使用
print("13: ", end=' ')
print(type(x))
print("15: x =", x)

x=add(7)# 打包功能块可以先只传递一个变量,返回新的function
print("18:",type(x))
x=x(8)  # 再传递另外一个变量
print("20: x = ", x)
