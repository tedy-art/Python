rows = 10
b = 0
for i in range(1,rows+1, 2):
    b += 1
    for j in range(1, i+1):
        print(b, end=" ")
    print()