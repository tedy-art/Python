a = int(input("Enter a number : "))

print('-'*20)
for i in range(1,11):
    print("|{m:^5}|{n:^5}|{l:^5}|".format(m=a, n=i, l=a*i))
print("-"*20)