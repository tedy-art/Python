my_list = [10,20.5,'SAI',True,10+20j,'SAI']
my_list.append([10, 20.5, "INSTAGRAM", 30])
print(my_list)
# [10, 20.5, 'SAI', True, (10+20j), 'SAI', [10, 20.5, 'INSTAGRAM', 30]]

FindTAG = my_list[-1][2][3:6]
print(FindTAG)