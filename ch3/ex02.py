#!/usr/bin/env python
# EX 02: create a new list with 3 random integers as elements

import random

def main():
    lista = []
    for _ in xrange(3):
        lista.append(random.randint(1, 100))
    print(lista)

if __name__ == '__main__':
    main()
