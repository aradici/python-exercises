#!/usr/bin/env python

# EX 01: create a new list with 3 random strings as elements

import random

def main():

	lista = []
	# I begin creating an empty list called lista
	
	# I decided to use a for cycle to generate the new list.
	# it was used _ instead of x so _ will not memorize the return of range
	for _ in range(3):
		lista.append(random.choice('abcdefghijklmnopqrstuvwxyz'))

	print lista

if __name__ == '__main__':
    main()




