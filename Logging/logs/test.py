from logger import logging
def add(a, b):
    logging.debug("Addition")
    return a+b
print(add(10, 15))