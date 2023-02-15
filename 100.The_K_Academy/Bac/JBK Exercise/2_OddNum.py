"""
Write a program to accept number from user and find it is odd number
"""

# Sol 1: with ==
inp_num = int(input("Enter 1st number :"))

if inp_num % 2 == 1:
    print("Number is odd")

# sol 2: with !=
inp_num1 = int(input("Enter sec number :"))

if inp_num1 % 2 != 0:
    print("Number is odd")

# sol 3: with function
def Odd_Num(inp_num2):
    if inp_num2 % 2 == 1:
        print("Number is odd")


inp_num2 = int(input("ENter 3rd Number : "))
Odd_Num(inp_num2)