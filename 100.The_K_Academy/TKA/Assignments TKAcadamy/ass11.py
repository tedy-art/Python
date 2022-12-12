n = 5

print(id(n))
for i in range(1, n+1):
    for i in range(1, i+1):
        print('*', end=" ")
    print()