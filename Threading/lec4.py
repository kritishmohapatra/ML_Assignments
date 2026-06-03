from concurrent.futures import ProcessPoolExecutor
import time
def sq(num):
    time.sleep(2)
    return f"sq is : {num**2}"
numbers=[1, 2, 3, 4, 5]
if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=3) as exe:
        res=exe.map(sq, numbers)
    for r in res:
        print(r)