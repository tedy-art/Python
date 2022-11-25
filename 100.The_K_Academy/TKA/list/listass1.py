my_list = [10,20.5,'SAI',True,10+20j,'SAI']
my_list.append([10, 20, "INSTAGRAM", 30])
print(my_list)
sec_list = my_list[-1]
print(sec_list)

third_list = sec_list[2]
print(third_list)

Find_TAG = third_list[3:6]
print(Find_TAG)