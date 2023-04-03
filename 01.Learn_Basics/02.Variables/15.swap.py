from os import *
from sys import *
from collections import *
from math import *

def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b
a = int(input())
b = int(input())
swap()