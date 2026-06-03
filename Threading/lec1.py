##Multi
import threading
import time

def print_n():
    for i in range(5):
        time.sleep(2)
        print(f"Num:{i}")
def print_l():
    for i in "abcde":
        time.sleep(2)
        print(f"letter:{i}")
t1=threading.Thread(target=print_n)
t2=threading.Thread(target=print_l)
t=time.time()
t1.start()
t2.start()

t1.join()
t2.join()
print("finished", time.time()-t)
