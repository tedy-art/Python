l = [33, 66, 7,3,22,5]
min = l[0]

for i in range(1, len(l)):
    if min > l[i]:
        min = l[i]

print(min)