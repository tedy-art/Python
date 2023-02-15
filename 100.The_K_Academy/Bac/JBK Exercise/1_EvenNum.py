""" Write a program to accept number from user and find it is Even"""

# Solution 1
print("Solution 1 : with == ")
input_num = int(input("ENter number : "))

if input_num % 2 == 0:
    print("Number is even.")

# Solution 2 : with function
def even_num(input_num1):
    if input_num1 % 2 == 0:
        print("Number is Even.")
    else:
        print("Number is Odd.")
input_num1 = int(input("ENter 2nd number : "))
even_num(input_num1)