# Palindrome number
# Using simple Iteration
# num = 1221
# temp = num
# reverse = 0
# while temp > 0:
#     rem = temp%10
#     reverse = (reverse*10)+rem
#     temp = temp//10
#
# print()
# print("Using simple Iteration method")
#
# if num == reverse:
#     print(f"{num} is Palindrome")
# else:
#     print(f"{num} is Not palindrome")
#
# """
#     Using string slicing
# """
#
# num = 1234
# reverse = int(str(num)[::-1])
#
# print()
# print("Using simple string slicing method")
#
# if num == reverse:
#     print(f"{num} is Palindrome")
# else:
#     print(f"{num} is Not Palindrome")

def palindrome(temp3):
    rev = 0
    while temp3 > 0:
        rem = temp3%10
        rev = (rev*10)+rem
        temp3 = temp3//10
    if num3 == rev:
        print(f"{num3} is palindrome..")
    else:
        print("Number is not palindrome..")
num3 = int(input("Enter number : "))
temp3 = num3
palindrome(temp3)