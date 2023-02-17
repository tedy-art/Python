num1 = int(input("Number 1 : "))
num2 = int(input("Number 2 : "))

if num1 % 2 == 0 and num2 % 2 == 0:
    sum = num1 + num2
    print("Number is Even : ")
    print(f"Addition of {num1} and {num2} is {sum}")

elif num1 % 2 != 0 and num2 % 2 != 0:
    sum = num1 + num2
    print("Number is Odd : ")
    print(f"Addition of {num1} and {num2} is {sum}")

else:
    print("please check... both input value must be even or odd ...")