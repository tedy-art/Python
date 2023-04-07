from os import *
from sys import *
from collections import *
from math import *

# Start coding
def countBits(n):
    binary = bin(n)
    c = str(binary).count('1')
    return c

n = int(input())
print(countBits(n))