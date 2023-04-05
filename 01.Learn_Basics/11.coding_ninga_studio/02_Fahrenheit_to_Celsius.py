from os import *
from sys import *
from collections import *
from math import *

s = 20
e = 119
w = 13

# while s<=e:
#     c = (s-32)*5/9
#     print(s, end="\t")
#     print(int(c))
#     s += w

for i in range(s,e, w):
    c = (i-32)* 5/9
    if c < 0:
        c = ceil(c)
    else:
        c = floor(c)
    print(i,c,sep="\t")