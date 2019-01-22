"""
    Topics in Computer Systems
    HW1 - Due Tuesday, January 29
    Problem 2: Birthday attack on a 40-bit hash
    Group 11 - Maithri Harve, Alex Karacaoglu, Helina Belete, Kevin Tso, Kate Kitsakos
"""

import random
import hashlib
import string

hashDictionary = {}

# Generating ~random~ strings
# https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
def generateRandomString():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

def calculateHashValue(s):
    return hashlib.sha1(s.encode('utf-8')).hexdigest()

def performBirthdayAttack():
    count = 0
    while True:
        count += 1
        s = generateRandomString()
        hashValue = calculateHashValue(s)[0:10]
        if hashValue in hashDictionary:
            return ("String 1: " + s, "String 2: " + hashDictionary[hashValue], "First 10 of common hash value: " + hashValue, "Number of calls to SHA1: " + str(count))
        else:
            hashDictionary[hashValue] = s

# Run the code!
# Two sets of examples that work:
# ('String 1: 4A3Y00XXKZ', 'String 2: X5BZHDNWFJ', 'First 10 of common hash value: 4819399339', 'Number of calls to SHA1: 1007791')
# ('String 1: KGRBLVRUBA', 'String 2: TBDH5461DK', 'First 10 of common hash value: 7fcdc4d357', 'Number of calls to SHA1: 363832')

print(performBirthdayAttack())
