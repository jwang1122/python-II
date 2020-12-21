from pymonad.operators.maybe import Just, Nothing
from pymonad.list import *
from rx import Observable,of, operators as op
from pymonad.reader import Compose

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

x = Just("John") >> shopping
print(x)

persons = of("John", "Wei", "Jun")
persons.subscribe(
    on_next = lambda i: print((Just(i) >> shopping).value),
    on_error = lambda e: print("Error Occurred: {0}".format(e)),
    on_completed = lambda: print("Done!\n"),
)

composed = persons.pipe(
    op.map(lambda x: shopping(x))
)
composed.subscribe(lambda value: print("Received: {0}".format(value)))
