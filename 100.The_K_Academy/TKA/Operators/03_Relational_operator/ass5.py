""" Find numbers from above list which is less than 100 and number must be odd or
    greater than and number must be even"""

l = [123, 45, -56, 98, 99, 100, 456, 89, 458]
for i in l:
    if i >= 100 and i%2 == 1 or i < 100 and i%2 == 0:
        print(i)