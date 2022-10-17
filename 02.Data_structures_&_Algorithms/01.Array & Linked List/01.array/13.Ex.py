"""
Write a python program to append a new item to the end of the array.
Simple o/p:
    original array : array('i',[1,3,5,7,9])
    Append 11 at the end of the array:
    New array: array('i',[1,3,5,7,9,11])
"""

import array as arr

a = arr.array('i',[1,3,5,7,9])
print("Original array : ", a)
print("Append 11 at the end of the array : ")
a.append(11)
print('New array : ', a)