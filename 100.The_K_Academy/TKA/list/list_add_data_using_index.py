my_list = [10, 20.5, 'SAI', True, (10+20j), 'SAI', [10, 20.5, 'INSTAGRAM', 30]]
new_list = my_list[3] = False
print(new_list)

my_list[-1][2] = 'FACEBOOK'
print(my_list)

print(my_list.pop())
print(my_list.pop(2))
print(my_list)

rem_list = my_list.remove(20.5)
print(rem_list)
print(my_list)