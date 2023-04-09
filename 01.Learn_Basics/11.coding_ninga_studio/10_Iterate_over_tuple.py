def iterate(t):
    # Write your code here.
    itr = iter(t)
    size = len(t)
    while size > 0:
        print(next(itr))
        size = size - 1

user_input = input().split(", ")
iterate(user_input)