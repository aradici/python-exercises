#!/usr/bin/env python
# 9) create a dictionary as (6), with 20 elements (possibly random) and order
# the dictionary by value

import operator
import random
import string

from functions import generate_key, generate_value

def main():
    dizio = dict()
    for _ in xrange(20):
        chiave = generate_key()
        while(dizio.has_key(chiave)):
            chiave = generate_key()

        dizio[chiave] = generate_value()
    dizio_sorted = sorted(dizio.items(), key=operator.itemgetter(1))
    print (dizio_sorted)

if __name__ == '__main__':
    main()
