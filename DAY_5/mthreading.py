import threading
import time

def worker(name: str, delay: float) -> None:
    for step in range(3):
        time.sleep(delay)
        print(f"Thread {name} is working on step {step+1}")

t1 = threading.Thread(target=worker, args=("A", 3))
t2 = threading.Thread(target=worker, args=("B", 1.5))

t1.start()
t2.start()

t1.join()
t2.join()

print("All threads finished")
