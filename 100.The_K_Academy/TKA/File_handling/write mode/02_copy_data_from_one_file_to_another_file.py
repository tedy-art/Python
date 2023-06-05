a = open("data.txt", "r")
b = open("geek.txt", "w")
for x in a:
    b.write(x)