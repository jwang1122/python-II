from pymonad import *
"""
Return boxed dictionary
"""
def isEven(x):
    if(x % 2 == 0):
        reason = {'status':'Success','message':"The x=%d mod of 2 is 0." % x}
        return Right(reason)
    reason = {'status':'Error','message':"The x=%d mod of 2 equals 1." % x}
    return Left(reason)

# unbox result
def parser(reason):
    print("Status:",reason.getValue()["status"]) # Open wrapper box by myself.
    print("Message:",reason.getValue()["message"])

y = 4
response = isEven(y)
parser(response)
y = 7
response = isEven(y)
parser(response)
