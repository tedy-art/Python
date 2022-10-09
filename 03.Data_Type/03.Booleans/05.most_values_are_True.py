# Almost any value in evaluted to true if it has some sort of content.
# Any string is true, except empty strings.
# Any number is true, except 0.
# Any list, tuple, set & dictionary are True, except empty ones.

print(bool("abc"))
print(bool(123))
print(bool(["apple","banana","cherry"]))