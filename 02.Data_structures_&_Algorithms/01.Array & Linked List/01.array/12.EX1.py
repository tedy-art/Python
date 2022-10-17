"""
Write a pytho program to create an array of 5 integers and display the array items,
Access through indexes
"""
import array as arr

a = arr.array('i',[1,3,5,7,9])
for x in a:
    print(x)

print("Access first three items individually: ")
print(a[0])
print(a[1])
print(a[2])