"""
write a python program to reverse the order of the items in the array.

simple o/p:
    original array : array('i',[1,3,5,3,7,1,9,3)
    Reverse the order of the items :
    array('i',[3,9,1,7,3,5,3,1])
"""
import array as arr

a = arr.array('i',[1, 3, 5, 3, 7, 1, 9, 3])
print("Original Array : ",a)

print("reverse the order of the items:")
a.reverse()
print(a)