num1 = eval(input("Enter first number : "))
num2 = eval(input("Enter second number : "))

while True:
    print('*'*50)
    print("\t Welcome to batch Calculator")
    print(('*'*50))

    print("""
            Menu
            + Addition
            - Substraction
            * Multiplication
            / Division
    """)
    Choise = input("Enter your Choice[+, -, *, /, //, **, <, >] : ")
    print(Choise)
    print('*'* 50)

    if Choise == '+':
        print(num1 + num2)

    elif Choise == '-':
        print(num1 - num2)

    elif Choise == '*':
        print(num1 * num2)

    elif Choise == '/':
        print(num1 / num2)

    elif Choise == '//':
        print(num1 // num2)

    elif Choise == '**':
        print(num1 ** num2)

    elif Choise == '<':
        print(num1 < num2)

    elif Choise == '>':
        print(num1 > num2)

    else:
        print("Invalid Input/ Oeration....")

    ch = input("Do you want to Continue[y/n] : ")
    if ch.lower() != 'y':
        break