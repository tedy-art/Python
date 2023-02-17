num1 = int(input("Number 1 : "))
num2 = int(input("Number 2 : "))

if num1%2 != 0 and num2%2 != 0:
    sum = num1 + num2
    print(f"addition of {num1} and {num2} is {sum}")

else:
    print("one of the number or one number is even.")