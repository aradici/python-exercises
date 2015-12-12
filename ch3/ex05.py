#!/usr/bin/env python
# EX 05: same exercise as (4), then remove the last element from list B (and only there)

import random

def main():
	lista = []
	for _ in xrange(3):
		lista.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
	lista2 = lista[:-1]
	print "this is the content of the original list: %s" % lista
	print "this is the content fo the copied list without the last element: %s" % lista2

if __name__ == '__main__':
    main()
