import array as arr

a = arr.array('d',[1.1,2.1,3.8,3.1,3.7,1.2,4.6])
print("All Values : ")
for x in a:
    print(x)
print("\n Specific values: ")
for x in a[1:3]:
    print(x)