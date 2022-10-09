thistpl = ("apple","banana","cherry")

# convert tuple to list
y = list(thistpl)

# remove item in the list "apple"
y.remove("apple")
thistpl = tuple(y)
print(thistpl)