import logging
log_format = '%(asctime)s %(levelname)s [%(name)s] - %(message)s::%(filename)s::%(lineno)d'
logging.basicConfig(filename='mylogs.log', filemode='w', level=logging.DEBUG, format=log_format)
logger = logging.getLogger('WANG')

from circle1 import circle_area

def
try:
    area = circle_area(3.2)
    print("10:",area)
    area = circle_area(-2)
    print("12:",area)
except ValueError as err:
    logger.info('Error: wrong input value')

print("Done.")