def odd_number_of_given_range(start, end):
    odd_number = []
    even_number = []
    for i in range(start, end+1):
        if i%2 != 0:
            odd_number.append(i)
        else:
            even_number.append(i)

    print(f"odd : {odd_number}")
    print(f"even : {even_number}")

# Start and end value
start = int(input("Enter start value :" ))
end = int(input("Enter end value : "))

# function call
odd_number_of_given_range(start, end)