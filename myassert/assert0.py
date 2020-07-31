def div(x,y):
    """
    if the condition is not meet, program stop running
    """
    assert y!=0, "divisor cannot be 0."
    return x/y

try:
    z = div(10,0)
except AssertionError as ae:
    print("Error: ", ae)



print("Done.")