from circle1 import circle_area

r = 1
try:
    area = circle_area(r)
    print("06:",area)
except Exception as err:
    print("08: Error-", err)

r=2.3
try:
    area = circle_area(r)
    print("13:",area)
except Exception as err:
    print("15: Error-",err)

try:
    area = circle_area(-2)
    print("19:",area)
except Exception as err:
    print('21: error: {0}'.format(err))

try:
    area = circle_area(-2+3j)   
    print("25:",area)
except TypeError as err:
    print("27: error: {0}".format(err))


try:
    area = circle_area('hello')
    print("32:",area)
except TypeError as err:
    print("34: error: {0}".format(err))

try:
    area = circle_area(None) 
    print("38:",area)
except TypeError as err:
    print("40: error: {0}".format(err))

print("Done.")