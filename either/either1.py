from pymonad.either import Left, Right
"""
Return boxed dictionary
"""
def isEven(x):
    if(x % 2 == 0):
        reason = {'status':'Success','message':"The x=%d mod of 2 is 0." % x, 'value':True}
        return Right(reason)
    reason = {'status':'Error','message':"The x=%d mod of 2 equals 1." % x, 'value':False}
    return Left(reason)

# unbox result
def parser(reason):
    print(reason.either(lambda reason: reason.get('value'), lambda reason: reason.get('value')))
    print(reason.either(lambda reason: reason.get('message'), lambda reason: reason.get('message')))
    if reason.is_right:
        print("It is even number.")
    elif reason.is_left:
        print("It is odd number.")

if __name__ == '__main__':
    y = 4
    response = isEven(y)
    parser(response)
    y = 7
    response = isEven(y)
    parser(response)
