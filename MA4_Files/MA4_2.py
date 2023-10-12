#!/usr/bin/env python3

from person import Person
from numba import njit
from time import perf_counter as pc
import matplotlib.pyplot as plt

@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return (fib_numba(n-1) + fib_numba(n-2))
	
def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))

def main():
	f = Person(5)
	start = pc()
	# print(f.get())
	# f.set(7)
	# print(f.get())
	print(fib_numba(10))
	end = pc()
	print(fib_py(10))
	end2 = pc()
	print(start - end)
	print(end - end2)
	print(f.fib())


if __name__ == '__main__':
	main()
