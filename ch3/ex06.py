#!/usr/bin/env python
# EX 06: create a dictionary with 3 random keys and 3 random strings as elements

import random

def main():
	dizio = {}
	for _ in xrange(3):
		dizio[random.randint(1,1000)] = random.choice('abcdefghjklmnopqrstuvwxyz')
	print dizio
# I have a problem here, I dunno how to make a condition to be sure that the key is not
# already created because the key must be unique in the dictionary

if __name__ == '__main__':
    main()
