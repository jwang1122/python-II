"""
isEven() function return Either Right or Left based on input value.

if the input number is even, return Right
else return Left
write output to log file "mylogs.log"
"""
import logging
log_format = '%(asctime)s %(levelname)5s [%(name)s] - %(message)s::%(filename)s::%(lineno)d'
logging.basicConfig(filename='mylogs.log', filemode='w', level=logging.DEBUG, format=log_format)
logger = logging.getLogger('WANG')

from pymonad import *

def isEven(x):
    if(type(x) not in [int]):
        reason = ('Error', 'The input value {0} is not an interger.'.format(x))
        return Left(reason)
    if(x % 2 == 0):
        reason = ('Success',"The x=%d mod of 2 is 0." % x)
        return Right(reason)
    reason = ('Error',"The x=%d mod of 2 equals 1." % x)
    return Left(reason)

def handler(x):
    if(type(x)==Left):
        logger.error(x)
    else:
        logger.info(x)
    

handler * isEven(4)
handler * isEven(7)
handler(isEven(3.2))
handler(isEven(3+2j))
handler(isEven(-2))