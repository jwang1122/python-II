import inspect
import os
f = inspect.currentframe()
i = inspect.getframeinfo(f)

def div(x,y):
    """
    if the condition is not meet, program stop running
    """
    assert y!=0, "divisor cannot be 0."
    return x/y

try:
    z = div(10,0)
except AssertionError as ae:
    print(f"{inspect.getframeinfo(f).lineno}: {'Error: ', ae}")



print("Done.")