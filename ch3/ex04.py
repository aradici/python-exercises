#!/usr/bin/env python
# EX 04: create list A with 3 strings as elements, copy it to list B

import random

def main():
	lista = []
	for _ in xrange(3):
		lista.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
	lista2 = lista[:]
	print "this is the content of the original list: %s" % lista
	print "this is the content of the copied list: %s" % lista2

if __name__ == '__main__':
    main()
