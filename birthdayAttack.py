"""
    Topics in Computer Systems
    HW1
    Problem 2: Birthday attack on a 40-bit hash
"""

import random
import hashlib
import string

hash_dictionary = {}

# How to generate random strings
# https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
# ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

def generate_random_string():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

def calculate_hash_value(s):
    return hashlib.sha1(s.encode('utf-8')).hexdigest()

# Two sets that work:
# ('String 1: 4A3Y00XXKZ', 'String 2: X5BZHDNWFJ', 'First 10 of common hash value: 4819399339', 'Number of calls to SHA1: 1007791')
# ('String 1: KGRBLVRUBA', 'String 2: TBDH5461DK', 'First 10 of common hash value: 7fcdc4d357', 'Number of calls to SHA1: 363832')
def go():
    count = 0
    while True:
        count += 1
        s = generate_random_string()
        hash_value = calculate_hash_value(s)[0:10]
        if hash_value in hash_dictionary:
            return ("String 1: " + s, "String 2: " + hash_dictionary[hash_value], "First 10 of common hash value: " + hash_value, "Number of calls to SHA1: " + str(count))
        else:
            hash_dictionary[hash_value] = s
