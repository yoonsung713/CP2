from time import perf_counter as pc
from time import sleep as pause
import random
import functools
import concurrent.futures as future

def approximation(n, d):
    cnt = 0
    for _ in range(n):
        num_of_d = [random.uniform(-1, 1) for _ in range(d)]
        sum = functools.reduce(lambda a, b : a + b, list(map(lambda x : x**2, num_of_d)))
        if sum <= 1:
            cnt += 1
    return cnt / n * (2 ** d)

if __name__ == "__main__":
    start = pc()
    approx = 0
    procs = []
    n = 10000000
    d = 11
    n_per_proc = [n//10 for _ in range(10)]
    d_per_proc = [d for _ in range(10)]

    with future.ProcessPoolExecutor() as ex:
        procs = ex.map(approximation, n_per_proc, d_per_proc)
        approx = sum(procs) / 10

    end = pc()
    print(f"1.3 approximation: {approx}")
    print(f"Process took {round(end-start, 2)} seconds")

# import random
# import math
# import functools

# def volume(d, r):
#     return ((math.pi) ** (d / 2)) / (math.gamma(d / 2 + 1)) * r ** d

# def approximation(n, d):
#     cnt = 0
#     for _ in range(n):
#         num_of_d = [random.uniform(-1, 1) for _ in range(d)]
#         sum = functools.reduce(lambda a, b : a + b, list(map(lambda x : x**2, num_of_d)))
#         if sum <= 1:
#             cnt += 1
#     return cnt / n * (2 ** d)

# print(volume(2, 1))
# print(approximation(100000, 2)) 
# print("---------")
# print(volume(11, 1))
# print(approximation(100000, 11)) 

