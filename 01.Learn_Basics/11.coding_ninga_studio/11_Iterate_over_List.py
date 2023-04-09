def iterate(l):
    # Write your code here.
    itr = iter(l)
    size = len(l)
    while size > 0:
        print(next(itr))
        size = size - 1

user_input = input().split(", ")
iterate(user_input)