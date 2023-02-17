print("""
        1: Sunday
        2: Monday
        3: Tuesday
        4: Wednesday
        5: Thursday
        6: Friday
        7: Saturday
    """)

choice = int(input("User Input : "))
if choice == 1:
    print("Sunday")

elif choice == 2:
    print("Monday")

elif choice == 3:
    print("Tuesday")

elif choice == 4:
    print("Wednesday")

elif choice == 5:
    print("Thursday")

elif choice == 6:
    print("Friday")

elif choice == 7:
    print("Saturday")

else:
    print("Invalid input..")