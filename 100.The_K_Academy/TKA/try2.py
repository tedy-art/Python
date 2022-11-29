# l = [1,2,3,[4,5,6,['rahul','rajesh','raghi']]]
# k = l[3][3][0:3]=["ram","Sham","Akshay"]
# print(k)
# print(l)
# a, b = k
# l[-1][-1][0:1] = a,b
# print(l)

# *********************Extend()*************************
# l1 = [1,2,3]
# l2 = ['rahul','rajesh','raghu']
# l3 = l1.extend(l2)
# print(l1)

# ********************** for ********************************
# l2 = ["rahul", "amit", "rajesh", "raghu", "pratik"]
# for i in l2:
#     if i[0] == 'r':
#         print(i)
#
# l2 = (22, 44, 11, 99)
# for i in l2:
#     print(i)

# *******************************************************************
l2 = set()
l2.add((11,22,88,56))
print(l2)
print(l2.pop())
print(l2)