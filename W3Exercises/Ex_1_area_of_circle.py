"""
Write a Python program that calculates the area of a circle based on
the radius entered by the user.
Sample Output:
r = 1.1
sample Output:
Area = 3.8013271108436504
"""
# Solution 1
from math import pi
r = 1.1
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


# Solution 2
r = 1.1
pi = 3.14

area_of_circle = pi*r*r
print(f"Area of Circle : {area_of_circle}")