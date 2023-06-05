f = open("hello.txt", mode="r", buffering= 10)
if f:
    print("opened")
print(f)