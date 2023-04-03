num = int(input("Enter number : "))
sum = 0
temp = num
while temp > 0:
    rem = temp % 10
    sum += rem * rem * rem
    temp = temp//10

if num == sum:
    print(f"{num} is an armstrong number..")
else:
    print("Number is not armstrong number..")