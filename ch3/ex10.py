#!/usr/bin/env python
# 10) create a dictionary with strings as key and tuple as elements

import random
import string

from functions import generate_key, generate_value

def main():
    dizio = dict()
    for _ in xrange(5):
        chiave = generate_key()
        while(dizio.has_key(chiave)):
            chiave = generate_key()

        dizio[chiave] = (generate_value(), generate_value())
    print (dizio)

if __name__ == '__main__':
    main()
