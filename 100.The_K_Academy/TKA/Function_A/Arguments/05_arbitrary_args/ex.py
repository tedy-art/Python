l = [54,98,56,32,65,87]

l1=list(filter(map(lambda x : (x%2==1), l)))
print(l1) 


l2 = list(filter(map(lambda x : True if x % 2 == 0 else False), l))
print(l2)