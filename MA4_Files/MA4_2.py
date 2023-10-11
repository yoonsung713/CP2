#!/usr/bin/env python3

from person import Person

def main():
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())
	print(f.fib(5))

if __name__ == '__main__':
	main()
