l = [123, 195, 111, 45, 300, 254, -56, 98, 99, 100, 456, 89, 458]
g_list = []
l_list = []
for i in l:
    if i >= 100 and i <= 300:
        g_list.append(i)
    else:
        l_list.append(i)

print(g_list)
print(l_list)