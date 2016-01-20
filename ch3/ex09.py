#!/usr/bin/env python
# 9) create a dictionary as (6), with 20 elements (possibly random) and order
# the dictionary by value

import operator
import random
import string

CHOICE = string.ascii_letters + string.digits

def randomstring(times, chars):
    s = ''
    for _ in xrange(times):
        s += random.choice(chars)
    return s

def generate_key():
    key = random.randint(1, 1000)
    return key

def generate_value():
    value = randomstring(random.randint(5, 15), CHOICE)
    return value

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
