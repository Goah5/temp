from random import *
import time

def txpo1(N):
    return sum(range(1, N+1))

def txpo2(N):
    return N * (N + 1) / 2

a = 100000

FList = [txpo2]
for n, f in enumerate(FList, start=1):
	
    start = time.time()
    for i in range(250):
        t = f(a)
    end = time.time()
    print(n, "	", end - start)



