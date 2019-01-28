"""
    Topics in Computer Systems
    HW1 - Due Tuesday, January 29
    Problem 2: Birthday attack on a 40-bit hash
    Group 9 - Maithri Harve, Alex Karacaoglu, Helina Belete, Kevin Tso, Kate Kitsakos
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
            print("First 10 of the common hash value: " + hashValue)
            return (s, hashDictionary[hashValue], str(count))
        else:
            hashDictionary[hashValue] = s

print(performBirthdayAttack())
