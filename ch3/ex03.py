#!/usr/bin/env python
# EX 03: create a new list with 1 integer and 2 strings as elements

import random
import string

def randomstring(times, chars):
    s = ''
    for _ in xrange(times):
        s += random.choice(chars)
    return s

def main():
    lista = []
    lista.append(random.randint(1,100))
    for _ in xrange(2):
        stringa = randomstring(random.randint(5,15), string.ascii_letters+string.digits )
        lista.append(stringa)
    print lista

if __name__ == '__main__':
    main()
