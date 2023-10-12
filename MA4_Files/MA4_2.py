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
	# f = Person(5)
	# start = pc()
	# print(f.get())
	# f.set(7)
	# print(f.get())
	# print(fib_numba(10))
	# end = pc()
	# print(fib_py(10))
	# end2 = pc()
	# print(start - end)
	# print(end - end2)
	# print(f.fib())
	ns = list(range(30, 46))  # Values of n from 30 to 45
	py_times = []
	numba_times = []
	cpp_times = []

	for n in ns:
		start = pc()
		fib_py(n)
		end = pc()
		py_times.append(end - start)
		
		start = pc()
		fib_numba(n)
		end = pc()
		numba_times.append(end - start)
		
		f = Person(n)
		start = pc()
		f.fib()
		end = pc()
		cpp_times.append(end - start)

	plt.figure()
	plt.plot(ns, py_times, label="Python")
	plt.plot(ns, numba_times, label="Numba")
	plt.plot(ns, cpp_times, label="C++")
	plt.xlabel("n")
	plt.ylabel("Time (seconds)")
	plt.legend()
	plt.savefig("fibonacci_performance.png")
	plt.close()


if __name__ == '__main__':
	main()
