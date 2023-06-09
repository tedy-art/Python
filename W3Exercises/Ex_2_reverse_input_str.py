"""
Write a Python program that accepts the user's first and last name
and prints them in reverse order with a space between them
Sample Input:-
tejas falke
Sample Output:-
eklaf sajet
"""
def rev_name(fname, lname):
    rev_f_str = fname[::-1]
    rev_l_str = lname[::-1]
    print(f"reverse str : {rev_l_str} {rev_f_str}")

# User's input
first_name = input("Enter your first name : " )
last_name = input("Enter your last name : " )
# Calling function
rev_name(first_name, last_name)