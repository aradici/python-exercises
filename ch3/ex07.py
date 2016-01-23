#!/usr/bin/env python
# same as (6), remove the last element and, for the same key in the dictionary,add a list with 3 strings as elements

import random
import string

from functions import randomstring, generate_key, generate_value

def main():
    dizio = dict()
    for _ in xrange(3):
        chiave = generate_key()
        valore = generate_value()
        while(dizio.has_key(chiave)):
            chiave = generate_key()

        dizio[chiave] = generate_value()
    dizio[chiave] = [generate_value(), generate_value(), generate_value()]
    print (dizio)

if __name__ == '__main__':
    main()
