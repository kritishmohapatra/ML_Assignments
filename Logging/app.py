import logging
logging.basicConfig(

    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers={
        logging.FileHandler("app1.log"), 
        logging.StreamHandler()
    }
)

logger=logging.getLogger("Arithmetic ")
def add(a, b):
    logger.debug(f"adding {a}+{b} is {a+b}")
    return a+b
def sub(a, b):
    logger.debug(f"subtacting {a}-{b} is {a-b}")
    return a-b
def mul(a, b):
    logger.debug(f"multiplicating {a}*{b} is {a*b}")
    return a*b
def div(a, b):
    try:
        res=a/b
        logger.debug(f"dividing {a}/{b} is {res}")
        return res
    except ZeroDivisionError:
        logger.error("Division by zero")
        return None
    
add(10, 20)
mul(10, 20)
sub(10, 30)
div(10, 5)