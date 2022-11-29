# l = [12, 67, 45.98, 'rajesh','rahul']
# print(l[-2],l[1])
# print(l[-2:-5:-2])
# print(l[-2][2:6])
# print(l[-1][1:3])
#
# print(l.index('rahul'))
# print(l[4][::-2])
#
# l.append([11, 22, 33, 44])
# print(l)
# <----------------------------25/11/2022---------------------------->
# l = [22, 55, 66, 88]
# l.insert(1,999)
# # print(l2)
# print(l)
# l.pop(-2)
# print(l)
#
# l.remove(999)
# print(l)

# 45 -> 84
# l = [22,"instagram", 55, 66, 88,[23,45,67]]
# l[-1][0] = 'Ram'
# l[-1][1] = 'Sham'
# print(l)

l = [22,"instagram", 55, 66, 88,[23,45,67,[12,45,78,[98,72,87]]]]
k = l[5][3][3]
print(k)
k.remove(98)
print(l)
l[-1][-1][-1][0] = 'RAM','sham'
print(l)