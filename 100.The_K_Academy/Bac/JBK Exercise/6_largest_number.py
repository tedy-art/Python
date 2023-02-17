num1 = int(input("Enter Number : "))
num2 = int(input("Enter Number : "))

if num1 > num2:
    print(f"{num1} is largest.")
elif num2 > num1:
    print(f"{num2} is largest.")
else:
    print(f"{num1} and {num2} are equal number.")