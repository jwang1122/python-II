"""
为什么我们要把变量打包，
其中原因之一，就是避免未定义的变量导致程序运行终止（blow up）。
另一个原因，就是希望能够完成功能块链式运作的过程，
在运行过程中，所有变量都可以自动完成解包和打包的动作，
如果运行出现意外，或者使用Maybe获得预先设定的默认值，
或者使用Either.Left返回错误信息。
"""
from pymonad.operators.maybe import Just, Nothing
from pymonad.tools import curry

@curry(2)
def add(x, y):
    return x + y

a = Just(6) 
#a = Nothing # instead of using None, we use Maybe.Nothing(wrapper None)
x = add * a & Just(9) #Applicative
print(x)

# 正常情况下，如果有一个输入变量没有定义，则整个程序爆掉中断。
# a = None
# x = add(a, 10) # in case the variable 'a' is not defined, the application will blow up.
# print(x)
# print("Done.")