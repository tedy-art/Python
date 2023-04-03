### "Split()"

Create a new variable that contains a string of fruits separated by commas. 
Use the split() method to divide the string into smaller pieces, 
or substrings, at each comma, and store the resulting substrings in a new list. 
This will create a new index for each fruit in the list, allowing you to access 
each fruit separately.

e.g.,

    fruits = "apple, banana, orange"
    fruits_list = fruits.split(",")
    print(fruits_list)

O/p:

    ['apple', 'banana', 'orange']

e.g. 
Que. find area of rectangle
    
    # Get input value from user with space
    in_value = input()
    # Assign in_vlaue to length and breadth and split()
    length, breadth = in_value.split()
    # Type Converting string into int
    length = int(length)
    # Type Converting string into int
    breadth = int(breadth)
    # Area of ractangle
    area = (length * breadth)
    # print output
    print(area)

O/p:

    4 20
    80