from math import pi
from pymonad.either import *

def circle_area(radius):
    if type(radius) not in [int, float]:
        reason = {'status':'Error', 'message':f'The input value {radius} is not an interger or real number.'}
        return Left(reason)
    if radius < 0:
        reason = {'status':'Error', 'message':f'The radius cannot be negative, but {radius}.'}
        return Left(reason)
    area = pi * radius * radius    
    reason = {'status':'Success', 'message':f'The area with given radius {radius} is {area}.', 'value':area}
    return Right(reason)

if __name__ == '__main__':
    eitherResult = circle_area(1)
    if eitherResult.is_right:
        print(eitherResult.value.get("message"))

    eitherResult = circle_area(-2)
    if eitherResult.is_left:
        print(eitherResult.either(lambda reason: reason.get('message'), lambda reason: reason.get('message')))

    eitherResult = circle_area(2)
    print(eitherResult.either(lambda reason: reason.get('message'), lambda reason: reason.get('value')))

    eitherResult = circle_area(2+3j)
    print(eitherResult.either(lambda reason: reason.get('message'), lambda reason: reason.get('message')))

    print("Done.")