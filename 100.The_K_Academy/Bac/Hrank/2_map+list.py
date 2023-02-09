numbers = [2, 4, 6, 8, 10]

# returns the square of a number
def square(number):
  return number * number

# apply square() to each item of the numbers list
squared_numbers_iterator = map(square, numbers)

# converting to list
squared_numbers = list(squared_numbers_iterator)
print(squared_numbers)

# Output: [4, 16, 36, 64, 100]