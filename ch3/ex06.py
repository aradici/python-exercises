#!/usr/bin/env python
# EX 06: create a dictionary with 3 random keys and 3 random strings as elements

import random
import string
from functions import randomstring, generate_key, generate_value

def main():
    dizio = dict()
    for _ in xrange(3):
        chiave = generate_key()
        while(dizio.has_key(chiave)):
            chiave = generate_key()

        dizio[chiave] = generate_value()        
    print (dizio)

if __name__ == '__main__':
    main()
