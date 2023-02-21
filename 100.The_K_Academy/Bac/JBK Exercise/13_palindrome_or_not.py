# Palindrome number
# Using simple Iteration
num = 1221
temp = num
reverse = 0
while temp > 0:
    rem = temp%10
    reverse = (reverse*10)+rem
    temp = temp//10

print()
print("Using simple Iteration method")

if num == reverse:
    print(f"{num} is Palindrome")
else:
    print(f"{num} is Not palindrome")

"""
    Using string slicing
"""

num = 1234
reverse = int(str(num)[::-1])

print()
print("Using simple string slicing method")

if num == reverse:
    print(f"{num} is Palindrome")
else:
    print(f"{num} is Not Palindrome")