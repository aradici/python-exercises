#!/usr/bin/env python
# functions created for chapter 3's exercises

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

def add_newvalue(existingkey, newvalue, dictionary):
    if existingkey in dictionary:
        oldvalues = dictionary[existingkey]
        dictionary[existingkey] = [ oldvalues, 'newvalue' ]
        print("the key already exists so I'm adding the new value to the old one")
    else:
        dictionary[existingkey] = newvalue
    return dictionary
