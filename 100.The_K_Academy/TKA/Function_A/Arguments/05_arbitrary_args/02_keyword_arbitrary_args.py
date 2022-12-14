def add_num(**kwargs):
    print(kwargs)
    print(type(kwargs))

add_num(num1 = 10, num2 = 20)
add_num(num1 = 10, num3 = 30, num4 = 30, num2 = 100)