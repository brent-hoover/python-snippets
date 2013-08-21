#!/usr/bin/env python
import random
import string
import hashlib
import binascii

def create_random_crap(num_chars):
    crap_string = ''
    seed = string.ascii_letters + string.digits + string.punctuation
    for x in range(0, num_chars):
        rnd = int(random.uniform(0, 52))
        random_char = seed[rnd:rnd+1]
        crap_string += random_char
    return crap_string

if __name__ == '__main__':
    x = create_random_crap(512)
    print(x)