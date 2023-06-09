"""
 Write a Python program to calculate the sum of three given numbers.
 If the values are equal, return three times their sum
"""
# a = int(input("Enter a :"))
# b = int(input("Enter b :"))
# c = int(input("Enter c :"))
#
# if a == b == c:
#     print((a+b+c)*3)
# else:
#     print(a+b+c)

def sum_three_num(a, b, c):
    if a == b == c:
        print((a+b+c)*3)
    else:
        print(a+b+c)

a = int(input("Enter a :"))
b = int(input("Enter b :"))
c = int(input("Enter c :"))
sum_three_num(a, b, c)