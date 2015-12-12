#!/usr/bin/env python
# EX 03: create a new list with 1 integer and 2 strings as elements

import random

def main():
	lista = []
	lista.append(random.randint(1,100))
	for _ in xrange(2):
		lista.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
	print lista

if __name__ == '__main__':
    main()
