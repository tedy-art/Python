"""
Write a Python program that accepts a sequence of comma-separated numbers from the
user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""
# input
# print(input)
# convert input into list
# print(list)
# convert list into tuple
# print(tuple)

in_user = input("Enter number: ").split(",")
print(list(in_user))
print(tuple(in_user))