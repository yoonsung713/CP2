#!/usr/bin/env python3

from person import Person
from numba import njit
from time import perf_counter as pc
import matplotlib.pyplot as plt

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))
	

@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return (fib_numba(n-1) + fib_numba(n-2))


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
	n_4 = list(range(30, 45))  # Values of n from 30 to 45
	f = Person(3)
	py_times = []
	numba_times = []
	cpp_times = []

	for n in n_4:
		start = pc()
		fib_py(n)
		end = pc()
		py_times.append(end - start)
		print(py_times)
		
		start = pc()
		fib_numba(n)
		end = pc()
		numba_times.append(end - start)
		print(numba_times)
		
		f.set(n)
		start = pc()
		f.fib()
		end = pc()
		cpp_times.append(end - start)
		print(cpp_times)

	plt.figure()
	plt.plot(n_4, py_times, label="Python")
	plt.plot(n_4, numba_times, label="Numba")
	plt.plot(n_4, cpp_times, label="C++")
	plt.xlabel("n")
	plt.ylabel("seconds")
	plt.legend()
	plt.savefig("py_numba_cpp.png")
	plt.close()

	n_5 = list(range(20, 30))  # Values of n from 20 to 30
	py_times2 = []
	numba_times2 = []

	for n in n_5:
		start = pc()
		fib_py(n)
		end = pc()
		py_times2.append(end - start)
		
		start = pc()
		fib_numba(n)
		end = pc()
		numba_times2.append(end - start)

	plt.figure()
	plt.plot(n_5, py_times2, label="Python")
	plt.plot(n_5, numba_times2, label="Numba")
	plt.xlabel("n")
	plt.ylabel("seconds")
	plt.legend()
	plt.savefig("py_numba.png")
	plt.close()

	f.set(47)
	print(f"if n = 47 -> numba: {fib_numba(47)}, cpp: {f.fib()}")
	'''
	The reason why cpp is negative is because it is out of the int range of cpp
	'''

if __name__ == '__main__':
	main()
