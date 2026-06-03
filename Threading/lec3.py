from concurrent.futures import ThreadPoolExecutor
import time 

def p_n(num):
    
    time.sleep(1)
    return f"num is :{num}"
nu=[1, 2, 3, 4, 5]
with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(p_n, nu)
for res in results:
    print(res)