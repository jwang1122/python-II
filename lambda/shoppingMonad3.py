from pymonad.operators.maybe import Just, Nothing

# 完成了链式反应，但若出错，整个运行中断在错误输出。
def writeShoppingList(x):
    # if(x=="Wei"):
    #     raise ValueError("Wei is not supported...")
    return Just(x+" prepare shopping list.")

def driveToMarket(x):
    return Just(x+"\nDrive to the market.")

def findThing(x):
    return Just(x + "\nFind stuff need to buy.")

def checkout(x):
    return Just(x + "\nCheck out, pay credit card.")

def driveBackHome(x):
    return Just(x + "\nDrive home.")
    
def shopping(x):
    return Just(x) \
        >> writeShoppingList \
        >> driveToMarket \
        >> findThing \
        >> checkout \
        >> driveBackHome

persons = ("David", "Jun", "Elle")
todos = list(map(lambda x: shopping(x), persons))

for i in todos:
    print(i)
