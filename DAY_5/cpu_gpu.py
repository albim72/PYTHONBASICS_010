from timeit import default_timer as timer
import numpy as np
from numba import jit,cuda

def cpufunction(a):
    for i in range(1000):
        a[i]+=1

@jit(nopython=True)
def jitfunction(a):
    for i in range(1000):
        a[i]+=1

if __name__ == '__main__':
    n = 1000
    a = np.ones(n,dtype=np.float64)
    start = timer()
    cpufunction(a)
    end = timer()
    print(f"CPU Time: {end-start}")

    start = timer()
    jitfunction(a)
    end = timer()
    print(f"JIT Time: {end-start}")
