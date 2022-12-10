L = []
sum = 0 

for i in range(20, 51):
    if i%2 != 0:
        sum += i
        print(sum)
        print(i)
        print(id(i))
        L.append(i)
print(L)
print(sum)