from os import *
from sys import *
from collections import *
from math import *




#Write your printDivisors function here.
def printDivisors(n):
    for i in range(1, n+1):
        if n%i == 0:
            print(i, end=" ")
        else:
            continue

n = int(input())
printDivisors(n)