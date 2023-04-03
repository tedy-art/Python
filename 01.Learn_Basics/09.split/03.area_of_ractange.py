# Get input value from user with space
in_value = input()
# Assign in_vlaue to length and breadth and split()
length, breadth = in_value.split()
# Type Converting string into int
length = int(length)
# Type Converting string into int
breadth = int(breadth)
# Area of rectangle
area = (length * breadth)
# print output
print(area)