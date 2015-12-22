#!/usr/bin/env python
# EX 04: create list A with 3 strings as elements, copy it to list B

import random
import string

def randomstring(times, chars):
    s = ''
    for _ in xrange(times):
        s += random.choice(chars)
    return s

def main():
    lista = []
    for _ in xrange(3):
        stringa = randomstring(random.randint(5,15), string.ascii_letters+string.digits )
        lista.append(stringa)
    lista2 = lista[:]
    print ("this is the content of the original list: {}".format(lista))
    print ("this is the content of the copied list: {}".format(lista2))

if __name__ == '__main__':
    main()
