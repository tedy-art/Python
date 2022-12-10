l = [23, -45, 10, 5, -8, 67, 478, -98, 55, 28]
l_new = []

for i in l:
    if i > 0:
        continue
    else:
        num = i * -1
        l_new.append(num)