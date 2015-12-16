#!/usr/bin/env python
# EX 01: create a new list with 3 random strings as elements

import random
import string

def rndstrng():
    stringarandom = ''
    for _ in xrange(10):
        stringarandom += random.choice(string.ascii_letters+string.digits)
    return stringarandom

def main():
    lista = []
    for _ in xrange(3):
            stringa = rndstrng()
            lista.append(stringa)
    print (lista)

if __name__ == '__main__':
    main()
