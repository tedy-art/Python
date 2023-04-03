"""
 We have strings "apple, Banana, Orange" & we want to split it at each comma
 ",", we can use split() method like below-->
"""
# Create a variable
fruits = "apple, banana, orange"
"""
Create a new variable that contains a string of fruits separated by commas. 
Use the split() method to divide the string into smaller pieces, or substrings,
at each comma, and store the resulting substrings in a new list. 
This will create a new index for each fruit in the list, allowing you to access 
each fruit separately.
 """
fruit_list = fruits.split(",")
print(fruit_list)