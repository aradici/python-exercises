#!/usr/bin/env python
# 8) starting from a dictionary as (6), create a method which has as inputs:
# "key" (the dictionary key), "value" (the value to add in the list present at 
# key) and the dictionary itself, make sure that the method adds key+element to 
# the dictionary or returns an error if it exists.

# Example for (8)
# starting with: dictionary['key'] = ['abc', 'ced', 'def']
# call: method('key', 'newvalue', dictionary)
# then the dictionary has: dictionary['key'] = ['abc', 'ced',
#                                               'def', 'newvalue']

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

def main():
    dizio = dict()
    for _ in xrange(3):
        chiave = generate_key()
        while(dizio.has_key(chiave)):
            chiave = generate_key()

        dizio[chiave] = generate_value()
    print (dizio)
    add_newvalue(generate_key(), generate_value(), dizio)
    print (dizio)

if __name__ == '__main__':
    main()
