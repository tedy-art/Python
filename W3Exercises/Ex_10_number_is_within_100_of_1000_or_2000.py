"""
Write a Python program to test whether a number is within 100 of 1000 or 2000.
100 of 1000 or 2000.
1) 1st give us any value "num = 940".
2) we need to do the same subtraction as 1000-940 = 60.
3) "ans" must be absolute, so we use abs() function as abs(1000-num) <= 100 or abs(2000-num) <= 100.
"""

num = int(input("Enter : "))
if abs(1000 - num) <= 100 or abs(2000 - num) <= 100:
    print(True)
else:
    print(False)