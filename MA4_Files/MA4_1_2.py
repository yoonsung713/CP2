# import random
# import math

# def volume(d, r):
#     return ((math.pi) ** (d / 2)) / (math.gamma(d / 2 + 1)) * r ** d

# def approximation(n, d):
#     lst = []
#     cnt = 0
#     for _ in range(n):
#         num_of_d = []
#         for _ in range(d):
#             x = random.uniform(-1, 1)
#             num_of_d.append(x)
#         sum = 0
#         for data in num_of_d:
#             sum += data ** 2
#             lst.append(sum)
#         if sum <= 1:
#             cnt += 1
#     return (cnt / n) * 2 ** d

# print(volume(2, 1))
# print(approximation(100000, 2)) 
# print("---------")
# print(volume(11, 1))
# print(approximation(100000, 11)) 



import random
import math
import functools
from time import perf_counter as pc

def volume(d, r):
    return ((math.pi) ** (d / 2)) / (math.gamma(d / 2 + 1)) * r ** d

def approximation(n, d):
    cnt = 0
    start = pc()
    for _ in range(n):
        num_of_d = [random.uniform(-1, 1) for _ in range(d)]
        sum = functools.reduce(lambda a, b : a + b, list(map(lambda x : x**2, num_of_d)))
        if sum <= 1:
            cnt += 1
    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")
    return cnt / n * (2 ** d)


# print(volume(2, 1))
# print(approximation(100000, 2)) 
# print("---------")
print(volume(11, 1))
print(f"1.2 approximation: {approximation(1000000, 11)}") 