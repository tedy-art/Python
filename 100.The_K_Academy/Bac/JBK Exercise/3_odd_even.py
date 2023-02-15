"""
Write a Program to accept a number and find it is even or odd
"""
# sol 1: with "==" and "%"
input_number = int(input("Enter number : "))
if input_number % 2 == 0:
    print(f"{input_number} is even.")
else:
    print(f"{input_number} is odd.")

# Sol 2: With "!=" and " % "
input_number2 = int(input("Enter 2nd number : "))
if input_number2 % 2 != 0:
    print(f"{input_number2} is Odd.")
else:
    print(f"{input_number2} is even.")

# Sol 3: With function
def even_odd(input_number3):
    if input_number3 % 2 == 0:
        print(f"{input_number3} is Even.")
    else:
        print(f"{input_number3} is Odd.")

input_number3 = int(input("Enter 3rd number : "))
even_odd(input_number3)