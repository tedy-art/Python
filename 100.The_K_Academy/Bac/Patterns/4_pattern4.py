"""
5 5 5 5 5
5 5 5 5
5 5 5
5 5
5
"""
rows = 5

for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print(rows, end=" ")
    print()