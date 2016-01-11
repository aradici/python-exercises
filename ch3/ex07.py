#!/usr/bin/env python
# same as (6), remove the last element and, for the same key in the dictionary,add a list with 3 strings as elements

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
    chiave2 = generate_key()
    dizio = {
        chiave2:(generate_value(), generate_value(), generate_value())
    }
    for _ in xrange(2):
        chiave = generate_key()
        while(dizio.has_key(chiave)):
            chiave = generate_key()

        dizio[chiave] = generate_value()        
    print (dizio)

if __name__ == '__main__':
    main()
