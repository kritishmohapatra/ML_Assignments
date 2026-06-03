import multiprocessing
import time

def sq():
    for i in range(5):
        time.sleep(2)
        print(f"square of {i} is {i**2}")

def cb():
    for i in range(5):
        time.sleep(1.5)
        print(f"cube of {i} is {i**3}")
if __name__=="__main__":
    p1=multiprocessing.Process(target=sq)
    p2=multiprocessing.Process(target=cb)
    t=time.time()
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"finished time:{time.time()-t}")