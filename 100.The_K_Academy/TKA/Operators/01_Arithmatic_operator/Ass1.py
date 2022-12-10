l = [2, 3, -20, 5, 4, 6, -89, -2, 100, 589, 652]
l_even = []
l_odd = []
for i in l:
    r = i % 2
    if r == 0:
        l_even.append(i)
    else:
        l_odd.append(i)
print("Even : ",l_even)
print("Odd : ", l_odd)
