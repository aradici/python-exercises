#!/usr/bin/env python
# EX 01: create a new list with 3 random strings as elements
import random

def main():

	lista = []

	for _ in range(3):
		lista.append(random.choice('abcdefghijklmnopqrstuvwxyz'))

	print lista

if __name__ == '__main__':
    main()




