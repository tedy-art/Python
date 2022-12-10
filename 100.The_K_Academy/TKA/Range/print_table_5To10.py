n1 = int(input("Enter start value : "))
n2 = int(input("Enter stop value : "))

for i in range(n1,n2+1):
    print("\n")
    for j in range(1,11):
        print(i*j, end=" ")