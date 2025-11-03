import math
import time
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def intensive_task(n: int) -> float:
    return sum(math.sqrt(i)for i in range(n*10_000_000))

if __name__ == '__main__':
    print("_____ ProcessPoolExecutor _________")
    start_process_time = time.time()
    with ProcessPoolExecutor() as executor:
        results = executor.map(intensive_task, range(10))
        for result in results:
            print(result)
    print(f"Process time (ProcessPoolExecutor): {time.time() - start_process_time}")

    print("_____ TreadPoolExecutor _________")
    start_thread_time = time.time()
    with ThreadPoolExecutor() as executor:
        results = executor.map(intensive_task, range(10))
        for result in results:
            print(result)

    print(f"Thread time (TreadPoolExecutor): {time.time() - start_thread_time}")
