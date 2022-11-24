# Immutable -> non-changeable

a = 10.8
print(a, type(a), id(a))

a = 10.9
b = 10.9
print(a, type(a), id(a))
print(b, type(b), id(b)) # memory re-use {see - memory allocation }