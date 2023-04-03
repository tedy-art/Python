from os import *
from sys import *
from collections import *
from math import *

principal = int(input())
rate = float(input())
time = int(input())
SI = principal * rate * time // 100
print(floor(SI))