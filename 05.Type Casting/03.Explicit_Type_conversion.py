"""
syntax:
<required_datatype>(expression)
"""
num_int = 123
num_str = "456"

print(type(num_int))
print(type(num_str))

#TYPE conversion str to int
num_str = int(num_str)
print(type(num_str))

#addition
num_sum = num_int + num_str
print(num_sum)
print(type(num_sum))