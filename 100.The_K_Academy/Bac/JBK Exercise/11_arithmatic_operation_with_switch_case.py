print("""
        + : Addition
        - : Subtraction
        * : Multiplication
        / : Division
        % : Modules
        ** : Exponentiation
        // : Floor Division
""")

num1 = int(input("Number 1 : "))
num2 = int(input("Number 2 : "))
Choice = input("Enter Your Choice [+, -, *, /, %, **, //] :-> ")

if Choice == '+':
    sum = num1 + num2
    print(sum)

elif Choice == '-':
    sum = num1 - num2
    print(sum)

elif Choice == '*':
    sum = num1 * num2
    print(sum)

elif Choice == '/':
    sum = num1 / num2
    print(sum)

elif Choice == '%':
    sum = num1 % num2
    print(sum)

elif Choice == '**':
    sum = num1 ** num2
    print(sum)

elif Choice == '//':
    sum = num1 // num2
    print(sum)

else:
    print("Invalid Input...")