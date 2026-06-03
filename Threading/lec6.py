import multiprocessing
import math 
import sys
import time

sys.set_int_max_str_digits(100000)

def fact(num):
    print(f"computing fact of {num}")
    res=math.factorial(num)
    print(f"fact  of {num} is {res}")
    return res

if __name__=="__main__":
    numbers=[5000, 6000, 700, 8000]
    start=time.time()
    with multiprocessing.Pool() as pool:
        results=pool.map(fact, numbers)
    end=time.time()

    print(f"results :{results}")
    print(f"time taken {end-start} in seconds")
